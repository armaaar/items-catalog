from universal import variables

# Create global meta variable
meta = type('', (), {})()
# default meta data
meta.title = variables.site_title
meta.body_class = variables.body_class
meta.description = variables.description
meta.keywords = variables.keywords
meta.seo_img = variables.seo_img



__all__ = ["home", "login", "logout"]
