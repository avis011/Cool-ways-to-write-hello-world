import time
import sys
def scroll_text(text):
  for char in str(text):
    sys.stdout.write(char)
    time.sleep(1.00)
    sys.stdout.flush()
  time.sleep(1.05)
scroll_text("Hello World")