articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los titulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los titulos usando un comprehensions"""
    return [article["title"] for article in articles if len(article["title"]) > 10]


def extract_article_summary(articles):
    return {
        article["title"]: article["title"]
        for article in articles
        if len(article["description"]) > 5
    }


print(extract_titles_traditional(articles))
print("=====")
print(extract_titles(articles))
print("=====")
print(extract_article_summary(articles))
