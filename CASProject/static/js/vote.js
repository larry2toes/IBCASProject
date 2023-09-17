function upvote(clicked){
    var postName = clicked.parentNode.parentNode.querySelector('.message-header').querySelector('.name').innerText;
    fetch("http://136.32.128.227:54321/upvote/" + postName, {
        method: "POST",
        body: JSON.stringify({
            id: "1"
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        }
    });
};