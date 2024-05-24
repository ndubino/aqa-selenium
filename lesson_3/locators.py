# Header
LOGO = ("xpath", "//div[contains(@class, 'text-logo')]")

EXPLORE_DROPDOWN = ("xpath", "//a[contains(@class,'nav-link dropdown')]")
EXPLORE_TOP_TRACKS = ("xpath", "//a[@click-event-part='explore_tracks_panel' and @click-event-target='Top tracks']")
EXPLORE_PYTHON = ("xpath", "//a[text()='Python' and contains(@click-event-part, 'explore')]")
EXPLORE_JAVA = ("xpath", "//a[text()='Java' and contains(@click-event-part, 'explore')]")
EXPLORE_GO = ("xpath", "//a[text()='Go' and contains(@click-event-part, 'explore')]")

PRICING_TAB = ("xpath", "//a[contains(@class, 'no-active router-link')]")
FOR_BUSINESS_TAB = ("xpath", "//li/a[(text()=' For Business ')]")

SIGN_IN_BUTTON = ("xpath", "//button[contains(@class,'btn btn-outline')]")
START_FOR_FREE_BUTTON = ("xpath", "//button[contains(@class,'btn btn-primary')]")

# Body
ALL_TRACKS_TAB = ("xpath", "//a[@click-event-context='{\"title\":\"all_tracks\"}']")
TOP_TRACKS_TAB = ("xpath", "//a[@click-event-context='{\"title\":\"top_tracks\"}']")
FRONTEND_TAB = ("xpath", "//a[@click-event-context='{\"title\":\"frontend\"}']")
GO_TAB = ("xpath", "//a[contains(@class,'active-route') and text()='Go ']")

ANDROID_TAB = ("xpath", "//a[text()='Android ']")

PYTHON_CORE_COURSE = ("xpath", "//a[@aria-label='Python Core']")
INTRODUCTION_TO_PYTHON_COURSE = ("xpath", "//a[@aria-label='Introduction to Python']")
KOTLIN_CORE_COURSE = ("xpath", "//a[@aria-label='Kotlin Core']")
INTRODUCTION_TO_JAVA_COURSE = ("xpath", "//a[@aria-label='Introduction to Java']")

# Здесь использовал индексы для привязке к расположению карточки
FIRS_CARD_IN_BLOCK = ("xpath", "//div[contains(@class,'col-md-6 col-12 mb-4 filtered-item')][1]")
SECOND_CARD_IN_BLOCK = ("xpath", "//div[contains(@class,'col-md-6 col-12 mb-4 filtered-item')][2]")

# Footer
TOP_TRACKS = ("xpath", "//a[@click-event-part='footer' and @click-event-target='Top tracks']")

REDDIT_LINK_ICON = ("xpath", "//a[@title='Hyperskill on Reddit']")
FACEBOOK_LINK_ICON = ("xpath", "//a[@click-event-target='Facebook']")
LINKEDIN_LINK_ICON = ("xpath", "//a[@click-event-target='Linkedin']")
DISCORD_LINK_ICON = ("xpath", "//a[@click-event-target='Discord']")

BLOG = ("xpath", "//a[@click-event-target='blog' and @click-event-part='footer']")
UNIVERSITY = ("xpath", "//a[@click-event-target='university' and @click-event-part='footer']]")

GOOGLE_PLAY_BUTTON = ("xpath", "//a[@click-event-target='google-play']")
APP_STORE_BUTTON = ("xpath", "//a[@click-event-target='app-store']")
