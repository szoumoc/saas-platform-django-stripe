import helpers

from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIRS = getattr(settings, "STATICFILES_VENDOR_DIRS", [])
# Use the first directory from the list or set a default path
from pathlib import Path
STATICFILES_VENDOR_DIR = Path(STATICFILES_VENDOR_DIRS[0]) if STATICFILES_VENDOR_DIRS else Path("static/vendors")


VENDOR_STATICFILES = {
    "flowbite.min.css": "vendors/flowbite.min.css",
    "flowbite.min.js": "vendors/flowbite.min.js",
}

class Command(BaseCommand): 
    def handle(self, *args, **kwargs):
        self.stdout.write("Hello, world! This is a custom management command in Django.")
        completed_urls = []
        for  name,url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )
