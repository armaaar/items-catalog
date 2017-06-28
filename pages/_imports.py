from flask import (render_template as r_t,
                   request, redirect, jsonify, url_for, flash,
                   session, make_response, g)
import universal

meta = type('', (), {})()


def set_page_info(title=None, body_class=None,
                  description=None, keywords=None, seo_img=None):
    global meta
    if title is None:
        meta.title = universal.variables.site_title
    else:
        meta.title = title

    if body_class is None:
        meta.body_class = universal.variables.body_class
    else:
        meta.body_class = body_class

    if description is None:
        meta.description = universal.variables.description
    else:
        meta.description = description

    if keywords is None:
        meta.keywords = universal.variables.keywords
    else:
        meta.keywords = keywords

    if seo_img is None:
        meta.seo_img = universal.variables.seo_img
    else:
        meta.seo_img = seo_img


def render_template(template, **kwargs):
    return r_t(template, universal=universal, meta=meta, **kwargs)


__all__ = ["universal", "set_page_info", "render_template", "request", "redirect", "jsonify", "url_for", "flash",
           "session", "make_response", "g"]
