import os
import lxml.etree as ET

def clean_tcx_content(tcx_file):
    with open(tcx_file, 'rb') as file:  # Open het bestand in binary-modus
        content = file.read()

    # Zoek naar de XML-declaratie en begin de inhoud vanaf daar
    start_index = content.find(b'<?xml')
    if start_index != -1:
        content = content[start_index:]

    return content

def tcx_to_gpx(tcx_file, gpx_file):
    try:
        # Reinig de inhoud van het TCX-bestand
        cleaned_content = clean_tcx_content(tcx_file)
        
        # Parse de gereinigde inhoud als XML
        tcx_root = ET.fromstring(cleaned_content)

        # Maak de root voor GPX
        gpx_root = ET.Element("gpx", version="1.1", creator="TCX-to-GPX Script")
        gpx_root.attrib['xmlns'] = "http://www.topografix.com/GPX/1/1"

        # Maak een GPX-track aan
        trk = ET.SubElement(gpx_root, "trk")
        name = ET.SubElement(trk, "name")
        name.text = os.path.basename(tcx_file).replace('.tcx', '')

        trkseg = ET.SubElement(trk, "trkseg")

        # Extraheer data van TCX en voeg toe aan GPX
        namespaces = {
            'tcx': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2',
        }
        trackpoints = tcx_root.findall('.//tcx:Trackpoint', namespaces)

        for tp in trackpoints:
            trkpt = ET.SubElement(trkseg, "trkpt")
            time = ET.SubElement(trkpt, "time")
            lat = tp.find('tcx:Position/tcx:LatitudeDegrees', namespaces)
            lon = tp.find('tcx:Position/tcx:LongitudeDegrees', namespaces)
            ele = tp.find('tcx:AltitudeMeters', namespaces)
            time_tcx = tp.find('tcx:Time', namespaces)

            if lat is not None and lon is not None:
                trkpt.attrib['lat'] = lat.text
                trkpt.attrib['lon'] = lon.text
            if ele is not None:
                elevation = ET.SubElement(trkpt, "ele")
                elevation.text = ele.text
            if time_tcx is not None:
                time.text = time_tcx.text

        # Schrijf het GPX-bestand
        gpx_tree = ET.ElementTree(gpx_root)
        gpx_tree.write(gpx_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")

        print(f"Converted {tcx_file} to {gpx_file}")
    except Exception as e:
        print(f"Failed to convert {tcx_file}: {e}")

def batch_convert_tcx_to_gpx(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.tcx'):
            tcx_file = os.path.join(directory, filename)
            gpx_file = os.path.join(directory, filename.replace('.tcx', '.gpx'))
            tcx_to_gpx(tcx_file, gpx_file)

if __name__ == "__main__":
    directory = input("Enter the directory containing TCX files: ")
    if os.path.isdir(directory):
        batch_convert_tcx_to_gpx(directory)
    else:
        print("The specified directory does not exist.")
