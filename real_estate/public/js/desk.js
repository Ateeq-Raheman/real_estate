console.log("HELLO DESK");

// // dom ready
// document.addEventListener("DOMContentLoaded", (event) => {
//     // navbar and anchor element
//     let navbar = document.querySelector(".navbar-collapse");
//     let anc = document.createElement('a');
//     anc.href = "https://erpnext.com";
//     anc.innerText = "Visit ERPNext";
//     navbar.prepend(anc);
// });

document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver(() => {
        const navbar = document.querySelector(".navbar-collapse");

        // Create the ytWidget div
        const ytWidgetDiv = document.createElement('div');
        ytWidgetDiv.id = "ytWidget";

        // Create the script tag
        const scriptTag = document.createElement('script');
        scriptTag.type = "text/javascript";
        scriptTag.src = "https://translate.yandex.net/website-widget/v1/widget.js?widgetId=ytWidget&pageLang=en&widgetTheme=dark&autoMode=true";

        // Append the ytWidget div and script tag to the navbar
        navbar.prepend(ytWidgetDiv);
        navbar.prepend(scriptTag);

        observer.disconnect();
    });
    observer.observe(document.body, { childList: true, subtree: true });
});


