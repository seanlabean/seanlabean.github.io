from glob import glob
from time import time
global INCL; INCL = "./inc"
global DEST; DEST = "./site"
global NAME; NAME = "S. C. Lewis"
global DOMAIN; DOMAIN = "www.sc-lewis.com"
global LICENSE; LICENSE = "NULL"
global TABLEOFCONTENTS; TABLEOFCONTENTS = "toc"

def lexicon():
    return glob(INCL+"/*.htm")

def init_site_file(lex_f):
    fn = lex_f.split('/')[-1]
    fn = fn.split('.')[0]
    with open(DEST+'/'+fn+'.html', 'w') as f:
        return f, fn

def write_header(f, fn, head, cat_dict):
    with open(DEST+'/'+fn+'.html', 'w') as f:
        f.write("<!DOCTYPE html><html lang='en'>")
        f.write("<meta charset='utf-8'/><meta name='viewport' content='width=device-width, inital-scale=1'/><link href='../links/main.css' type='text/css' rel='stylesheet'/><link href='../media/icon.png' type='image/png' rel='shortcut icon'/>")
        f.write("<title>" + NAME + "&mdash;" + fn + "</title></head>")
        f.write("<body>")
        if fn == "home":
            f.write("<header><a href='home.html'><img src='../media/main.png' width='160' height='80'></a>&nbsp;&nbsp;<img src='../media/refs/banner.png'></header>")
        else:
            f.write("<header><a href='home.html'><img src='../media/main.png' width='160' height='80'></a>&nbsp;&nbsp;<img src='../media/refs/banner.png'></header>")
        # can loop over header lines and do specific things based on contents
        #for line in head:
            #f.write(line)
        f.close()
    
def write_nav(f, fn, cat_dict):
    with open(DEST+'/'+fn+'.html', 'a') as f:
        f.write("<nav>\n")
        #f.write("<summary>Navigator</summary>\n")
        f.write("<section class='site-nav'>\n")
        #f.write("<section>\n<ul class='nobull'>\n<li><a href='home.html'>Back Home</a></li></ul>\n</section>\n")
        # find this filename as a value in the category dict. Return the category.
        match_cat = next((key for key, values in cat_dict.items() if fn in values), None)
        # make nav bar for each page. note which category the current page belongs AND mark current page in bar
        for cat, pages in cat_dict.items():
            if cat == 'no-proc': continue
            f.write("<section>\n")
            f.write("<h2 class='self'>"+cat+"</h2>\n") if cat == match_cat else f.write("<h2>"+cat+"</h2>\n")
            f.write("<ul class='nobull capital'>\n")
            for page in sorted(pages): f.write("<li><mark><a href='"+page+".html' class='self'>" + page + "</a></mark></li>\n") \
                if page == fn else f.write("<li><a href='"+page+".html'>" + page + "</a></li>\n")
            f.write("</ul>\n")
            f.write("</section>\n")

        f.write("</section>\n")
        f.write("</details></nav>\n")
        f.write("<!-- Generated file, do not edit -->\n")
    return

def write_toc_body(cat_dict):
    with open(DEST+'/'+TABLEOFCONTENTS+'.html', 'a') as f:
        f.write("<nav></nav>")
        f.write("<main>")
        f.write("<h2>The Garden at a Glance</h2>")
        f.write("<article><p>")
        f.write("<ul class='nobull'>")
        for page in sorted([value for values in cat_dict.values() for value in values]):
            f.write("<li><a href='"+page+".html'>"+page+"</a></li>")
        f.write("</ul>")
        f.write("</p></article></main>")
        f.close()

def parse_body(lex_f, fn, cat_dict):
    with open(lex_f) as inc:
        # SLICE out and process header lines
        inc_lines = inc.readlines()
        ind_head = [i for i, x in enumerate(inc_lines) if x == '---\n']
        if len(ind_head) == 2:
            # we have a header
            head = inc_lines[ind_head[0] + 1:ind_head[1]]
            body_lines = inc_lines[ind_head[1] + 1:]
        else:
            # no or erroneous head
            head = []
            body_lines = inc_lines
        inc.close()
    with open(DEST+'/'+fn+'.html', 'a') as f:
        write_header(f, fn, head, cat_dict)
        write_nav(f, fn, cat_dict)
        for line in body_lines:
            f.write(line)
        f.close()

def write_footer(fn):
    with open(DEST+'/'+fn+'.html', 'a') as f:
        f.write("<footer><hr />")
        #fpedited(f, srcpath)
        f.write("<b>Sean C. Lewis</b> © 2023 — ")
        f.write("<a href='" + LICENSE + "' target='_blank'>BY-NC-SA 4.0</a> — ")
        f.write("Assembled using <a href='https://github.com/seanlabean/astrea'>Astrea</a>")
        f.write("</footer>")
        f.write("</body>")
        f.write("</html>")

def preparse_header(lex_f, fn, categories):
    with open(lex_f) as inc:
        # SLICE out and process header lines
        inc_lines = inc.readlines()
        ind_head = [i for i, x in enumerate(inc_lines) if x == '---\n']
        if len(ind_head) == 2:
            # we have a header
            head = inc_lines[ind_head[0] + 1:ind_head[1]]
            try:
                cat = [i for i, x in enumerate(head) if x.split(':')[0] == 'category']
                this_cat = head[cat[0]].split(':')[-1].strip()
                categories.setdefault(this_cat, [])
                categories[head[cat[0]].split(':')[-1].strip()].append(fn)
            except IndexError:
                print(f"** {fn} - Incorrect header format.\nSetting category to 'no-proc'.\n")
                categories.setdefault('no-proc', [])
                categories['no-proc'].append(fn)    
        else:
            # no or erroneous head
            head = []
        inc.close()
    return categories

def write_table_of_contents(cat_dict):
    write_header(None, TABLEOFCONTENTS, [], cat_dict)
    write_toc_body(cat_dict)
    write_footer(TABLEOFCONTENTS)
    return
    
def finalize(f, fn):
    try:
        f.close()
    except:
        print(f"Error processing file {fn}")

def engine():
    lex = lexicon()
    # preprocess loop to get table of contents (which files belong to which categories)
    categories = {}
    tock = time()
    for lex_f in lex:
        f, fn = init_site_file(lex_f)
        preparse_header(lex_f, fn, categories)
    # make table of contents
    write_table_of_contents(categories)
    # main processing loop
    for lex_f in lex:
        f, fn = init_site_file(lex_f)
        parse_body(lex_f, fn, categories)
        write_footer(fn)
        finalize(f, fn)
    tick = time()
    print(f"Processed {len(lex)} files in {1000*(tick-tock):.5} miliseconds.")
if __name__ == "__main__":
    engine()