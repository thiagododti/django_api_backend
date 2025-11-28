# views.py
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status


class CookieTokenRefreshView(TokenRefreshView):
    """
    - Lê refresh de cookie 'refresh_token' se não vier no body.
    - Quando a resposta incluir 'refresh' (rotação ativada), escreve cookie HttpOnly.
    """
    cookie_name = 'refresh_token'
    cookie_path = '/api/token/refresh/'  # ajuste se precisar
    cookie_max_age = None  # opcional: definir em segundos ou usar exp do token

    def post(self, request, *args, **kwargs):
        # se não tiver no body, tenta pegar do cookie
        if 'refresh' not in request.data:
            cookie_refresh = request.COOKIES.get(self.cookie_name)
            if cookie_refresh:
                # muta request.data (Request.data pode ser QueryDict imutável em alguns casos)
                # construir um novo dict para passar ao serializer
                # hack simples; alternativamente construa serializer direto
                request._full_data = {'refresh': cookie_refresh}
        response = super().post(request, *args, **kwargs)

        # se a view retornou um novo refresh (ROTATE_REFRESH_TOKENS=True), gravar cookie HttpOnly
        if isinstance(response, Response) and response.status_code == status.HTTP_200_OK:
            resp_data = response.data
            new_refresh = resp_data.get('refresh')
            if new_refresh:
                # set cookie HttpOnly — ajuste secure=True em produção (HTTPS)
                response.set_cookie(
                    self.cookie_name,
                    new_refresh,
                    httponly=True,
                    secure=False,        # alterar para True em produção
                    samesite='Lax',
                    path=self.cookie_path,
                    # max_age=self.cookie_max_age,
                )
                # opcional: remover refresh do corpo se não quiser expor no JSON
                resp_data.pop('refresh', None)
                response.data = resp_data
        return response
