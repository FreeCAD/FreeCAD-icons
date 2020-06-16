"""FreeCAD icons

triplus 2020
"""

import uuid
import hashlib
import xml.etree.ElementTree as ET


def get_sha(file_name, block_size=65536):
    """Create and return sha."""
    sha = hashlib.sha256()
    with open("deploy/" + file_name + ".rcc", 'rb') as file_:
        while True:
            block = file_.read(block_size)
            if not block:
                break
            sha.update(block)

    return sha.hexdigest()


def update_xml():
    """Update metadata information (add sha)."""
    tree = ET.parse("Metadata/metadata.xml")
    themes = tree.getroot()

    for theme in themes:
        for elem in theme:
            if elem.tag == "name":
                sha = get_sha(elem.text)
                sub = ET.SubElement(theme, "sha")
                sub.text = sha
                print(elem.text)
                print(sub.text)

    tree.write("Metadata/metadata.xml")


update_xml()


# Metadata changed
ID = uuid.uuid4().hex
with open("deploy/metadata.txt", "w") as metadata_changed:
    metadata_changed.write(ID)
