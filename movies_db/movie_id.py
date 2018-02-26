from .base import MovieDB


class Movie(MovieDB):

    BASE_ENDPOINT = '/movie/{movie_id}'

    ACCOUNT_STATES = '/account_states'
    ALTERNATIVE_TITLES = '/alternative_titles'
    CHANGES = '/changes'
    CREDITS = '/credits'
    DETAILS = ''
    EXTERNAL_IDS = '/external_ids'
    IMAGES = '/images'
    KEYWORDS = '/keywords'
    LISTS = '/lists'
    RECOMMENDATIONS = '/recommendations'
    RELEASE_DATES = '/release_dates'
    REVIEWS = '/reviews'
    SIMILAR = '/similar'
    TRANSLATIONS = '/translations'
    VIDEOS = '/videos'

    def clean_response_data(self):
        return self.clean_item(self.response)

    def account_states(self):
        self.endpoint = self.BASE_ENDPOINT + self.ACCOUNT_STATES
        return self.get()

    def alternate_titles(self):
        self.endpoint = self.BASE_ENDPOINT + self.ALTERNATIVE_TITLES
        return self.get()

    def changes(self):
        self.endpoint = self.BASE_ENDPOINT + self.CHANGES
        return self.get()

    def details(self):
        self.endpoint = self.BASE_ENDPOINT + self.DETAILS
        return self.get()

    def external_ids(self):
        self.endpoint = self.BASE_ENDPOINT + self.EXTERNAL_IDS
        return self.get()

    def images(self):
        self.endpoint = self.BASE_ENDPOINT + self.IMAGES
        return self.get()

    def keywords(self):
        self.endpoint = self.BASE_ENDPOINT + self.KEYWORDS
        return self.get()

    def lists(self):
        self.endpoint = self.BASE_ENDPOINT + self.LISTS
        return self.get()

    def recommendations(self):
        self.endpoint = self.BASE_ENDPOINT + self.RECOMMENDATIONS
        return self.get()

    def release_dates(self):
        self.endpoint = self.BASE_ENDPOINT + self.RELEASE_DATES
        return self.get()

    def reviews(self):
        self.endpoint = self.BASE_ENDPOINT + self.REVIEWS
        return self.get()

    def similar(self):
        self.endpoint = self.BASE_ENDPOINT + self.SIMILAR
        return self.get()

    def translations(self):
        self.endpoint = self.BASE_ENDPOINT + self.TRANSLATIONS
        return self.get()

    def videos(self):
        self.endpoint = self.BASE_ENDPOINT + self.VIDEOS
        return self.get()
