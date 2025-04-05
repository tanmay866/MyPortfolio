import os
import sys
import re

# Debug statement
print("Starting website diagnostics...")

def print_header(text):
    print("\n" + "=" * 70)
    print(text)
    print("=" * 70)

def print_result(test, result, details=None):
    if result:
        print(f"✅ {test}")
    else:
        print(f"❌ {test}")
    
    if details:
        print(f"   {details}")

def check_file_exists(filepath, required=True):
    exists = os.path.exists(filepath)
    if required and not exists:
        return False, f"File not found: {filepath}"
    elif exists:
        size = os.path.getsize(filepath)
        if size == 0:
            return False, f"File exists but is empty (0 bytes): {filepath}"
        return True, f"File found ({size} bytes)"
    else:
        return True, "Optional file, not found but that's okay"

def check_js_libraries():
    # Read index.html to find script tags
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all script tags
        script_tags = re.findall(r'<script[^>]*src="([^"]*)"[^>]*>', content)
        
        missing = []
        found = []
        
        for src in script_tags:
            if src.startswith('http'):
                # External script - can't check directly
                found.append(f"External script: {src}")
            else:
                # Local script
                if os.path.exists(src):
                    size = os.path.getsize(src)
                    found.append(f"Local script: {src} ({size} bytes)")
                else:
                    missing.append(f"Missing script: {src}")
        
        return len(missing) == 0, {'missing': missing, 'found': found}
    
    except Exception as e:
        return False, f"Error checking JS libraries: {str(e)}"

def check_css_files():
    # Read index.html to find css links
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all link tags for CSS
        css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]*)"[^>]*>', content)
        
        missing = []
        found = []
        
        for href in css_links:
            if href.startswith('http'):
                # External CSS - can't check directly
                found.append(f"External stylesheet: {href}")
            else:
                # Local CSS
                if os.path.exists(href):
                    size = os.path.getsize(href)
                    found.append(f"Local stylesheet: {href} ({size} bytes)")
                else:
                    missing.append(f"Missing stylesheet: {href}")
        
        return len(missing) == 0, {'missing': missing, 'found': found}
    
    except Exception as e:
        return False, f"Error checking CSS files: {str(e)}"

def check_images():
    # Read index.html to find image tags
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all img tags
        img_tags = re.findall(r'<img[^>]*src="([^"]*)"[^>]*>', content)
        
        missing = []
        found = []
        
        for src in img_tags:
            if src.startswith('http'):
                # External image - can't check directly
                found.append(f"External image: {src}")
            else:
                # Local image
                if os.path.exists(src):
                    size = os.path.getsize(src)
                    found.append(f"Local image: {src} ({size} bytes)")
                else:
                    missing.append(f"Missing image: {src}")
        
        return len(missing) == 0, {'missing': missing, 'found': found}
    
    except Exception as e:
        return False, f"Error checking images: {str(e)}"

def run_checks():
    print_header("Tanmay Patel Portfolio - Website Diagnosis")
    
    print("\nChecking essential files...")
    core_files = {
        'index.html': True,
        'css/style.css': True,
        'js/main.js': True,
        'site.webmanifest': False,
        'assets/favicon.png': False,
        'assets/icon-192.png': False,
        'assets/icon-512.png': False,
        'assets/apple-touch-icon.png': False
    }
    
    all_essential_files_found = True
    for file, required in core_files.items():
        result, details = check_file_exists(file, required)
        print_result(f"Checking {file}", result, details)
        if required and not result:
            all_essential_files_found = False
    
    print("\nChecking JavaScript libraries...")
    js_result, js_details = check_js_libraries()
    print_result("JavaScript libraries", js_result)
    if isinstance(js_details, dict):
        if js_details.get('missing'):
            for m in js_details['missing']:
                print(f"   ❌ {m}")
        for f in js_details.get('found', []):
            print(f"   ✅ {f}")
    else:
        print(f"   {js_details}")
    
    print("\nChecking CSS files...")
    css_result, css_details = check_css_files()
    print_result("CSS files", css_result)
    if isinstance(css_details, dict):
        if css_details.get('missing'):
            for m in css_details['missing']:
                print(f"   ❌ {m}")
        for f in css_details.get('found', []):
            print(f"   ✅ {f}")
    else:
        print(f"   {css_details}")
    
    print("\nChecking images...")
    img_result, img_details = check_images()
    print_result("Images", img_result)
    if isinstance(img_details, dict):
        if img_details.get('missing'):
            for m in img_details['missing']:
                print(f"   ❌ {m}")
        for f in img_details.get('found', []):
            print(f"   ✅ {f}")
    else:
        print(f"   {img_details}")
    
    print_header("Diagnosis Summary")
    if all_essential_files_found and js_result and css_result and img_result:
        print("✅ All critical files appear to be in place.")
        print("✅ The website should work correctly.")
        print("\nIf you're still having issues:")
        print("1. Make sure you run the server from the correct directory")
        print("2. Check if port 8000 is already in use by another application")
        print("3. Try disabling your firewall temporarily")
        print("4. Make sure the Python HTTP server is allowed through your firewall")
    else:
        print("❌ There are some missing files or resources.")
        print("The website may not function correctly until these issues are fixed.")
    
    print("\nTo start the server, run: python serve.py")

if __name__ == "__main__":
    run_checks() 