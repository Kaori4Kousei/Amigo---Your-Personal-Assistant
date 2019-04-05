 if "open" in text:
        if "google" in text:
            print("Opening google.....")
            term = text[23:]
            url = "https://www.google.com/search?q={}".format(term)
            webbrowser.open_new_tab(url)
        elif "youtube" in text:
            print("Opening youtube....")
            term = text[22:]
            query_string = urllib.parse.urlencode({"search_query" : term})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            url = "http://www.youtube.com/watch?v={}".format(search_results[0])
            webbrowser.open_new_tab(url)
    elif "switch" in text:
        term = text[6:]
        print("Switching to {}.....".format(term))
        if __name__ == "__main__":
            results = []
            top_windows = []
            win32gui.EnumWindows(windowEnumerationHandler, top_windows)
            for i in top_windows:
                if term in i[1].lower():
                    win32gui.ShowWindow(i[0],5)
                    win32gui.SetForegroundWindow(i[0])
                    break