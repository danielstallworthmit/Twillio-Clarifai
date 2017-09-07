from clarifai.rest import ClarifaiApp
from appenv import CLARIFAI_API_KEY

app = ClarifaiApp(api_key=CLARIFAI_API_KEY)

def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])
    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])
    return tag_urls

print('\n'.join(get_relevant_tags('https://www.royalcanin.com/~/media/Royal-Canin/Product-Categories/dog-medium-landing-hero.ashx')))