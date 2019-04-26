import requests

def get_comic_title(browser):
    """Return the title text"""
    sel = "div#ctitle"
    title = browser.find_element_by_css_selector(sel)
    return title.text

def get_prev(browser):
    """Go to the previous comic"""
    #nav_buttons = browser.find_elements_by_css_selector(sel)
    #prev_button = nav_buttons[1]
    prev_button = browser.find_element_by_link_text("< Prev")
    prev_button.click()

def scrape_image(img, filename):
    """Save an image element as filename"""
    response = requests.get(img.get_attribute('src'))
    img_data = response.content
    with open(filename, 'wb') as f:
        f.write(img_data)

def find_image(browser):
    """Return the image element of the xkcd page."""
    sel = "div#comic img"
    img = browser.find_element_by_css_selector(sel)
    return img