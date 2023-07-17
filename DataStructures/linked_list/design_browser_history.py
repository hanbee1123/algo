"""
https://leetcode.com/problems/design-browser-history/

문제:
인터넷 브라우저에서 방문기록과 동일한 작동을 하는 Browser History class를 구현할 것이다. 
구현할 브라우저는 homepage에서 시작하고, 이후에는 다른 url에 방문할 수 있다.
또, 뒤로가기와 앞으로 가기가 작동하도록 구현하라.

- BrowserHistory(string homepage)를 호출하면 브라우저는 homepage에서 시작된다.
- void visit(string url)을 호출하면 현재 page의 앞에 있는 페이지기록은 다 삭제되고 url로 방문한다.
- string back(int steps)을 호출하면 steps수 마늠 뒤로가기를 할 수 있는 page개수가 x이고 step> x번 만큼만 뒤로가기를 한다.
뒤로 가기가 완료되면 현재 url을 return 한다.
- string forwards(int steps) 을 호출하면 steps수 만큼 앞으로 가기를 한다. 앞으로 갈 수 있는 page개수가 x이고 step> x라면 x번 만큼만 앞으로 가기를 한다.
앞으로 가기가 완료되면 현재 url을 return 한다.

제약조건: 
1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= step <= 100
homepage와 url은 .을 포함한 lower case 영어 문자로 구성되어 있다.
visit, back 그리고 forward는 최대 5000번의 호출 이 있을 수 있다.

input =
browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.back(2)
browserHistory.back(7)

output=
None
None
None
None
"facbook.com"
"google.com"
"facebook.com"
None
"linkedin.com"
"google.com"
"leetcode.com"

코드 설계:
1. page 클래스 만들기 (node)
class Page (self,url)
    class.url=url
    class.next=None
    class.prev=None

2. browserHistory 클래스 만들기
class browserHistory
    def __init__ (self, url:str): 
        newpage = Page(url)
        self.pointer = newpage
        self.length = 1
    
    def visit(url):
    # pointer 의 next는 newpage를 point해야함
        newpage = Page(url)

    def back
    # from the pointer, go backwards as the range of input
    case: input > length:

    def forward
    # from the pointer, go forwards as the range of input
    case: input is > length : 
"""

class Page:
    def __init__(self, url:str):
        self.url = url
        self.next = None
        self.prev = None

class browserHistory:
    def __init__(self, url:str):
        self.pointer = Page(url = url)
        self.length = 1

    def visit(self, url:str):
        self.pointer.next = Page(url=url, prev=self.pointer)
        self.pointer = self.pointer.next
        self.length += 1
        return None

    def back(self, index:int):
        while self.pointer.prev and index > 0:
            self.pointer = self.pointer.prev
            index -= 1
        return self.pointer.url

    def forward(self, index:int):
        while self.pointer.next and index > 0:
            self.pointer = self.pointer.next 
            index -= 1
        return self.pointer.url
    

if __name__ == '__main__':
    bh = browserHistory("leetcode.com");
    print(bh.visit("google.com")); 
    print(bh.visit("facebook.com"));
    print(bh.visit("youtube.com"));
    print(bh.back(1)); 
    print(bh.back(1));
    print(bh.forward(1));
    print(bh.visit("linkedin.com"));
    print(bh.forward(2));
    print(bh.back(2));
    print(bh.back(7));
    

## 이문제는 list로도 풀 수 있고, linked list로 풀수 있다.
# 하지만 list의 경우, visit 함수 때문에 사용이 힘들다.
# visit 함수는 새로운 url을 설정함과 동시에 그 앞의 모든 노드들을 지우게 된다.
# list의 경우 node를 지우는 operation이 비싸다. 하나하나 loop해가면서 지워야하기 때문에.
# linked list의 경우 앞의 노드를 참조하는 pointer가 없으면, GC에 의해 자동으로 지워진다.