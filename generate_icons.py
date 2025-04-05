import os
import base64

# Check if the assets directory exists
if not os.path.exists('assets'):
    os.makedirs('assets')

# SVG content from the logo.svg file
try:
    with open('assets/logo.svg', 'r') as f:
        svg_content = f.read()
except:
    print("Error: Could not read logo.svg file")
    exit(1)

# Generate favicon.ico HTML (browser will interpret this as the favicon)
favicon_html = f"""
<html>
<head>
<title>Favicon</title>
<link rel="icon" href="data:image/svg+xml;base64,{base64.b64encode(svg_content.encode()).decode()}">
</head>
<body style="background-color: #0A192F; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
    <div style="text-align: center; color: white;">
        <img src="data:image/svg+xml;base64,{base64.b64encode(svg_content.encode()).decode()}" style="width: 200px; height: 200px;">
        <h1 style="font-family: Arial; margin-top: 20px; color: #64FFDA;">Favicon Generated</h1>
        <p style="font-family: Arial;">This SVG is now being used as the favicon for your website.</p>
    </div>
</body>
</html>
"""

# Write favicon.html
with open('assets/favicon.html', 'w') as f:
    f.write(favicon_html)

# Generate a data URL version of the SVG for the favicon.png equivalent
favicon_data_url = f"""<html>
<head>
<title>Favicon Data URL</title>
</head>
<body style="background-color: #0A192F; color: white; font-family: Arial; padding: 20px;">
    <h1 style="color: #64FFDA;">Favicon Data URL</h1>
    <p>Copy the following data URL to use as a favicon:</p>
    <textarea style="width: 100%; height: 100px; background-color: #112240; color: white; padding: 10px; border: 1px solid #64FFDA;"
              onclick="this.select()">data:image/svg+xml;base64,{base64.b64encode(svg_content.encode()).decode()}</textarea>
    <p>To use this as a favicon, add the following code to your HTML:</p>
    <pre style="background-color: #112240; padding: 15px; border-left: 4px solid #64FFDA; overflow-x: auto;">
&lt;link rel="icon" href="data:image/svg+xml;base64,{base64.b64encode(svg_content.encode()).decode()}"&gt;
    </pre>
</body>
</html>
"""

# Write favicon_data_url.html
with open('assets/favicon_data_url.html', 'w') as f:
    f.write(favicon_data_url)

# Generate a placeholder file for favicon.png 
with open('assets/favicon.png', 'w') as f:
    f.write("<!-- This is a placeholder file. The actual favicon is implemented as a data URL in the HTML -->")

# Generate placeholder files for the other required icons
icons = ['icon-192.png', 'icon-512.png', 'apple-touch-icon.png']
for icon in icons:
    with open(f'assets/{icon}', 'w') as f:
        f.write(f"<!-- This is a placeholder file for {icon}. The actual favicon is implemented as a data URL in the HTML -->")

print("Generated favicon files in the assets directory:")
print("- favicon.html - Open this to see the favicon")
print("- favicon_data_url.html - Open this to get the data URL for the favicon")
print("- Created placeholder files for favicon.png, icon-192.png, icon-512.png, and apple-touch-icon.png")
print("\nNext step: Update your HTML to use the data URL favicon") 