var sendTag = function (eventName, elementId, cookieID) {
    var xhReq = new XMLHttpRequest();
    var URL = '';
    URL = "http://tag.blef.fr/equancy?event=" + eventName + '&elementID=' + elementId;
    if (cookieID != null) {
        URL += '&cookieID=' + cookieID;
    }
    xhReq.open("GET", URL, false);
    xhReq.send(null);
}