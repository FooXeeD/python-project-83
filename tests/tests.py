def test_page_name(client):
    response = client.get("/")
    string = "Анализатор страниц"
    bytes_data = string.encode('utf-8')
    assert bytes_data in response.data
