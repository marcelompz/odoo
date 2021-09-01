# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectosCustom(http.Controller):
#     @http.route('/proyectos_custom/proyectos_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyectos_custom/proyectos_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyectos_custom.listing', {
#             'root': '/proyectos_custom/proyectos_custom',
#             'objects': http.request.env['proyectos_custom.proyectos_custom'].search([]),
#         })

#     @http.route('/proyectos_custom/proyectos_custom/objects/<model("proyectos_custom.proyectos_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyectos_custom.object', {
#             'object': obj
#         })
