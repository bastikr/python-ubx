import os
import shutil

import ubx

# Make sure target directory exists
sourcedir = "source/"
if not os.path.exists(sourcedir):
    raise ValueError("sourcedir not found at {}".format(
        os.path.abspath(sourcedir)))

targetdir = os.path.join(sourcedir, "generated/message_descriptions")
if os.path.exists(targetdir):
    shutil.rmtree(targetdir)
os.makedirs(targetdir)

description_links = {}

for description in ubx.descriptions.default:
    name = description.name
    output = []
    output.append(".. _message-description-{}:\n".format(name))
    output.append(name)
    output.append("-"*len(name) + "\n")
    if not description.message_class.name in description_links:
        description_links[description.message_class.name] = []
    description_link = ":ref:`message-description-{}`".format(name)
    description_links[description.message_class.name].append((name, description_link))

    output.append(str(description))
    output.append("\n")

    targetpath = os.path.join(targetdir, name + ".rst")
    with open(targetpath, "w") as f:
        f.write("\n".join(output))
    # break

name = "message_descriptions.rst"
targetpath = os.path.join(targetdir, name)
with open(targetpath, "w") as f:
    f.write(".. _message_descriptions:\n\n")
    f.write("---------------------\n")
    f.write("Message Descriptions\n")
    f.write("---------------------\n\n")
    f.write(".. toctree::\n")
    f.write("   :maxdepth: 1\n")
    f.write("   :hidden:\n\n")

    toctree_entries = []
    content = []
    for key in sorted(description_links.keys()):
        content.append("\n" + key + "\n" + "-"*len(key))
        for name, link in sorted(description_links[key]):
            toctree_entries.append("   " + name)
            content.append("* " + link)

    f.write("\n".join(toctree_entries))
    f.write("\n\n")
    f.write("\n\n".join(content))
