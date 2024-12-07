import os

from dotenv import load_dotenv

load_dotenv()

DEVS = [
    1557184285,
    1087819304,
    7399365105
]

FKM = list(
    map(
        int,
        os.getenv(
            "FKM",
            "1557184285 7399365105",
        ).split(),
    )
)

API_ID = int(os.getenv("API_ID", "1634450"))

API_HASH = os.getenv("API_HASH", "1a42e816cae8d86e71a4c466bba19b8c")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7463343952:AAG2Mjk92xBHy9fAVlymRk_ZV0hwoAEp7R4")

OWNER_ID = int(os.getenv("OWNER_ID", "1557184285"))

FKM_ID = list(map(int,os.getenv("FKM_ID", "1557184285 7399365105",).split(),))

USER_ID = list(
    map(
        int,
        os.getenv(
            "USER_ID",
            "1557184285 7399365105",
        ).split(),
    )
)

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002031868588"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002031868588"))

BLACKLIST_CHAT = list(
    map(
        int,
        os.getenv(
            "BLACKLIST_CHAT",
            "-1001608847572 -1001538826310 -1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001861414061 -1001854052937 -1001638078842 -1001986858575",
        ).split(),
    )
)

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://dataceyprem:dataceyprem@cluster0.xt5qsmv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)

DB_NAME = os.getenv("DB_NAME", "rezaxkage")
