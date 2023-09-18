from django.contrib import sitemaps

class contactSiteMap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["/contact/"]

    def location(self, item):
        return item