async function currentArticleCount(){
    // Get total article count
    url = '/articles/jsonListView/';
    const response = await fetch(url)
    .then(res => res.json())
    .then(res => {
        return res;
    })

    var total = response.data.length;
    
    // Get current count
    var count = document.querySelectorAll(".card").length;
    var divs = document.querySelectorAll(".current-count");
    
    out = `
    <p>
        <small>
            <strong>
                Showing ${count} of ${total} posts
            </strong>
        </small>
    </p>
    `
    divs[0].innerHTML = out;
    divs[1].innerHTML = out;
}


async function loadMore(){
    url = '/articles/jsonListView/';
    const response = await fetch(url)
    .then(res => res.json())
    .then(res => {
        return res;
    })

    
    var currentPostCount = document.querySelectorAll(".card").length;
    var startIdx = currentPostCount;
    var postsToLoad = 4;
    
    const options = {year: 'numeric', month: 'short', day: 'numeric' };
    for (let i = startIdx; i < (startIdx + postsToLoad); i++){
    var obj = response.data[i];
    let publishDate = new Date(obj.publishDate).toLocaleDateString('en-us', options);

    let thumbnail = new URL(`https://fredducation.s3.amazonaws.com/${obj.thumbnail}`)

        if(obj.postType == "person" || obj.postType == "place"){
            out = `
                <a href="${obj.slug}">
                    <div class="card border-dark text-dark h-100">
                        <img class="card-img-top" 
                        src="${thumbnail}" 
                        alt="${obj.title} thumbnail">
                        <h4 class="card-title">
                            ${obj.title}
                        </h4>
                        <p class="card-subtitle">
                            ${obj.city},
                        </p>
                        <p class="card-subtitle">
                            ${obj.country}
                        </p>
                        <div class="card-footer">
                            ${publishDate}
                        </div>
                    </div>
                </a>
        `;
        } else {
            out = `
            <a href="${obj.slug}">
                <div class="card border-dark text-dark h-100">
                    <img class="card-img-top" 
                    src="${thumbnail}" 
                    alt="${obj.title} thumbnail">
                    <h4 class="card-title">
                        ${obj.title}
                    </h4>
                    <p class="card-subtitle">
                        ${obj.description}
                    </p>
                    <div class="card-footer">
                        ${publishDate}
                    </div>
                </div>
            </a>
            `;
        }
        
    var div = document.createElement("div");
    div.classList.add('col-6');
    div.classList.add('col-lg-3');
    div.innerHTML = out;
    document.getElementsByClassName('row')[0].appendChild(div);
    }  
}







