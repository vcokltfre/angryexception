from __future__ import annotations

import sys
from random import choice
from logging import getLogger
from os import getenv

from pyttsx3 import Engine, init  # type: ignore

logger = getLogger(__name__)

try:
    engine: Engine | None = init()
except OSError as e:
    engine = None
    logger.debug(f"Unable to load TTS engine: {e}")

if getenv("AE_DISABLE", "false").lower() == "true":
    engine = None

def install() -> None:
    if not engine:
        return

    def _excepthook(_, __, ___) -> None:  # type: ignore
        if not engine:
            return

        engine.say(  # type: ignore
            choice(
                [
                    "You're really stupid.",
                    "What's wrong with you?",
                    "You're an idiot.",
                    "You need to learn to program.",
                    "You must be the type of person that thinks one plus one is three.",
                ]
            )
        )
        engine.runAndWait()

    sys.excepthook = _excepthook
