import os

PRODUCTION=os.getenv('PRODUCTION', False)
MIXPANEL_TOKEN=os.environ.get('MIXPANEL_TOKEN')
