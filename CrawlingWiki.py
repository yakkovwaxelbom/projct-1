import urllib.parse
import requests
import random
import os
from bs4 import BeautifulSoup


def path_image(url_img, dir_path):  # פה אנחנו יוצרים נתיב הכולל שם לתמונה שאנחנו שומרים
    image_name = url_img.rsplit('/', 1)[1]
    file_path = os.path.join(dir_path, image_name)
    return file_path


def get_title(url):  # פה אנחנו יוצרים כותרת של דף
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.replace(' - Wikipedia', '')
        return title


def download_img(img_url, path):  # פונקציה להורדת תמונה אני מגדיר איזה תמונה להוריד ואיפה להוריד בהתמאה
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
    except:
        pass


def get_random_image(url, max_wanted_img):  # בהינתן URL אני מקבל את URL של התמונות
    images_url = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")  # אני מקבל גישה לקרוא את הטקסט
        all_images = soup.findAll('img', class_="mw-file-element")  # אני מוצא את כל התגיות של התמונות
        randomly_sampled_images = random.sample(all_images, min(len(all_images), max_wanted_img))
        for image in randomly_sampled_images:
            src = image.get('src')  # אני מתרגם את התווית URL
            if src.startswith('//'):
                src = "https:" + src
            elif src.startswith('/'):
                src = urllib.parse.urljoin(url, src)
            images_url.append(src)
        return images_url


def random_urls(url, max_wanted_urls, visited_links):  # בהינתן URL של ויקיפדיה אני מקבל עוד לינקים רנדומלים מאותו הדף
    links_url = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        all_urls = soup.find_all('a', href=True)
        randomly_sampled_urls = random.sample(list(set(all_urls) - visited_links), min(len(all_urls), max_wanted_urls))
        for link in randomly_sampled_urls:
            reference = link.get('href')
            if reference.startswith("/wiki"):
                links_url.append(urllib.parse.urljoin(url, reference))
        return links_url


def crawl_wiki(url, directory, depth, width, image_width, visited_links: set):
    visited_links.add(url)
    image_link = get_random_image(url, image_width)  # מחזירה רשימה של URL מוכנים להורדה
    path_title = get_title(url)
    current_directory = f"{directory}/{path_title}"
    os.makedirs(current_directory, exist_ok=True)
    for link in image_link:
        file_path = path_image(link, current_directory)
        download_img(link, file_path)
    page_link = random_urls(url, width, visited_links)
    for link in page_link:
        if depth > 0:
            crawl_wiki(link, directory, depth - 1, width, image_width, visited_links)


def main():
    crawl_wiki("https://en.wikipedia.org/wiki/Pablo_Picasso", '/home/mefathim/PycharmProjects', 2, 2, 20, set())


if __name__ == "__main__":
    main()
