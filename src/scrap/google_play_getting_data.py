"""
### Data Scraping
Para fazer o scraping dos dados do Google Play Store, iremos utilizar a biblioteca [google-play-scraper](https://github.com/JoMingyu/google-play-scraper).

Google-Play-Scraper fornece APIs para facilmente obter dados do Google Play Store utilizando Python sem dependências externas.

"""
import os
import sys
from get_app_info import get_app_info
from get_reviews import get_reviews
from sentiment_conversion import to_sentiment

APPS_IDS = ['com.zzkko', 'com.shopee.br', 'com.mercadolibre', 'com.novapontocom.casasbahia',
            'com.luizalabs.mlapp', 'com.b2w.americanas', 'com.alibaba.aliexpresshd',
            'com.amazon.mShop.android.shopping', 'com.schibsted.bomnegocio.androidApp',
            'br.com.enjoei.app']
SIZE = 2000

def main() -> int:
    apps_ids = os.environ.get('APPS_IDS', APPS_IDS)
    app_infos_df = get_app_info(apps_ids)
    print(app_infos_df)

    app_reviews_df = get_reviews(apps_ids, SIZE)
    # cria uma nova coluna 'sentiment' no dataframe
    app_reviews_df['sentiment'] = app_reviews_df.score.apply(to_sentiment)

    app_reviews_df.to_csv('reviews.csv', index=None, header=True)
    return 0

if __name__ == '__main__':
    sys.exit(main())