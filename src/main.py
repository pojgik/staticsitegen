from textnode import *
from htmlnode import *
from InlineTransformations import *
from BlockTransformations import *
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def copy_static(source, target):
    if not os.path.exists(target):
        os.mkdir(target)
    
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        target_item = os.path.join(target, item)
        
        if os.path.isfile(source_item):
            shutil.copy(source_item, target_item)
            print(f"Copied: {source_item} to {target_item}")
        else:
            copy_static(source_item, target_item)
            
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    template = open(template_path).read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
        


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory")
    copy_static(dir_path_static, dir_path_public)
    
    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )
    
    
if __name__ == '__main__':
    main()