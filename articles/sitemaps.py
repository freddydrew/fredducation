from django.contrib import sitemaps

class articleSiteMap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["/articles/"]

    def location(self, item):
        return item