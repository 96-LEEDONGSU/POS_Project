document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");
    const searchResults = document.getElementById("searchResults");
    
    searchInput.addEventListener("input", function () {
        const query = searchInput.value.toLowerCase();
        const elementsWithText = document.querySelectorAll(":not(script):not(style):not(meta):not(title):not(link):not(br):not(hr)");
        
        searchResults.innerHTML = ""; // 검색 결과 초기화
        
        elementsWithText.forEach(function (element) {
            const text = element.textContent.toLowerCase();
            if (text.includes(query)) {
                const resultItem = document.createElement("li");
                resultItem.textContent = text;
                
                // 검색어와 일치하는 부분을 하이라이트
                const highlightedText = text.replace(new RegExp(query, 'gi'), match => `<span class="highlight">${match}</span>`);
                resultItem.innerHTML = highlightedText;
                
                // 검색어와 일치하는 부분으로 스크롤 이동
                resultItem.addEventListener("click", function () {
                    element.scrollIntoView({ behavior: "smooth", block: "center" });
                });
                
                searchResults.appendChild(resultItem);
            }
        });
    });
});