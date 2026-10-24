import pytest


@pytest.mark.asyncio
async def test_health_check(cliente_http):
    resposta = await cliente_http.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_registrar_e_logar_usuario(cliente_http):
    email = "pytest@empresa.com"

    resposta_registro = await cliente_http.post(
        "/auth/registrar", json={"email": email, "senha": "senha123"}
    )
    assert resposta_registro.status_code == 201

    resposta_login = await cliente_http.post(
        "/login",
        data={"username": email, "password": "senha123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert resposta_login.status_code == 200
    assert "access_token" in resposta_login.json()


@pytest.mark.asyncio
async def test_registrar_e_logar_usuario(cliente_http, email_unico):
    resposta_registro = await cliente_http.post(
        "/auth/registrar", json={"email": email_unico, "senha": "senha123"}
    )
    assert resposta_registro.status_code == 201
    ...
