async function loadMore(){
    url = '/articles/jsonListView/';
    const response = await fetch(url)
    .then(res => res.json())
    .then(res => {
        return res;
    })

    var currentPostCount = document.querySelectorAll(".card").length;
    console.log(currentPostCount)
    var startIdx = currentPostCount;
    var postsToLoad = 4;

    const options = {year: 'numeric', month: 'short', day: 'numeric' };

    for (let i = startIdx; i < (startIdx + postsToLoad); i++){
        var obj = response.data[i]
        if(obj.postType == "person" || "place"){
            out = `
                <a href="${obj.slug}">
                    <div class="card border-dark my-2 text-dark h-100">
                        <img class="card-img-top" 
                        src="/${obj.thumbnail}" 
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
                            ${new Date(obj.publishDate).toLocaleDateString('en-us', options)}
                        </div>
                    </div>
                </a>
        `
        } else {
            out = `
            <a href="${obj.slug}">
                <div class="card border-dark my-2 text-dark h-100">
                    <img class="card-img-top" 
                    src="/${obj.thumbnail}" 
                    alt="${obj.title} thumbnail">
                    <h4 class="card-title">
                        ${obj.title}
                    </h4>
                    <p class="card-subtitle">
                        ${obj.description}
                    </p>
                    <div class="card-footer">
                        ${new Date(obj.publishDate).toLocaleDateString('en-us', options)}
                    </div>
                </div>
            </a>
            `
        }
        
    var div = document.createElement("div");
    div.classList.add('col-6')
    div.classList.add('col-lg-3')
    div.innerHTML = out
    document.getElementsByClassName('row')[0].appendChild(div);
    }  
}







