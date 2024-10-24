import os

def generate_homepage(directory='xc_data-main/womens_team', output_file='home.html'):
    # List all .html files in the given directory
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

    # Create the content for the homepage HTML page
    page_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cross Country Team Home</title>
    <link rel="stylesheet" href="../xc_data-main/css/style.css">
</head>
<body>
    <a href="#main-content">Skip to Main Content</a>
    <nav>
        <ul>
            <li><a href="index.html">Home Page</a></li>
            <li><a href="mens.html">Men's Team</a></li>
            <li><a href="womens.html">Women's Team</a></li>
        </ul>
    </nav>
    <header>
        <h1>Skyline Cross Country Team</h1>
    </header>
    <main id="main-content">
        <section>
            <h2>Athletes Overview</h2>
            <ul class="athlete-list">
'''
    # Add each athlete to the list
    for file in html_files:
        # Extract the athlete's name from the filename (assuming format: "First_Last.html")
        name = file.replace('_', ' ').replace('.html', '')
        page_content += f'                <li><a href="womens_team/{file}">{name}</a></li>\n'

    # Close the HTML tags
    page_content += '''            </ul>
        </section>
    </main>
    <footer>
        <p>Skyline High School Cross Country Team</p>
        <address>
            2552 North Maple Road, Ann Arbor, MI 48103<br>
            <a href="https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
            Follow us on Instagram <a href="https://www.instagram.com/a2skylinexc/" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </address>
    </footer>
</body>
</html>'''

    # Write the content to the output HTML file
    with open(f'xc_data-main/{output_file}', 'w') as f:
        f.write(page_content)

# Example usage
generate_homepage(output_file='home.html')
