from flask import render_template as r_t, request, redirect, jsonify, url_for, flash, session, make_response
import universal


def render_template(template, **args):
    return r_t(template, universal=universal, **args)

__all__ = ["render_template", "request", "redirect", "jsonify", "url_for", "flash",
    "session", "make_response", "universal"]
