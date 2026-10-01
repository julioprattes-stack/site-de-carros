import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def get_car_ai_bio(model, brand, year):
    prompt = (
        f'Me mostre uma descrição de venda para o carro {brand} {model} {year} '
        f'em apenas 250 caracteres. '
        f'Fale coisas específicas desse modelo de carro.'
    )

    try:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=150,
        )
        return response.choices[0].message.content
    except Exception:
        return ''