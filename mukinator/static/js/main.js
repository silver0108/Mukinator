function typing(query) {

  let content;
  if (query == ".text1") {
    content =
      "아으... 머리야.. \
      \n 지니녀석..갑자기 사라지던데..\
      \n 햇볕이 갑자기 따가워 진 것을 당신은 느낍니다.\
      \n\n 주위를 둘러보니 당신은 사막의 한복판임을 알았습니다.\
      \n 저 멀리 보이는 오아시스에서 당신이 먹고싶은 그 음식이 있었습니다."
  } else if (query == ".text2") {
    content =
      "앗 오아시스인 줄 알았는데..?\
    \n 오아시스인 줄 알았지만,\
    \n 물과 음식 대신 쪽지가 든 유리병이 놓여져 있습니다..\
    \n\n 앗 쪽지에 무언가 적혀져 있습니다.\
    \n확인해보니 쪽지에는 다음과 같이 적혀져 있습니다."
  } else if (query == ".text3") {
    content =
      "걷다보니 멀리 누군가가 보입니다.\
    \n 혼자가 아니라는 생각에 가까이 다가가려는데\
    \n 도적떼가 저를 보고 뛰어오고 있습니다.\
    \n\n 위험하다는 생각에 전력을 다해 도망가는데\
    \n 무언가에 걸려 넘어지고 말았습니다.\
    \n 뭔가 하고 보니 이상하게 생긴 책이 있었습니다.\
    \n 책을 펼치니 다음과 같이 적혀있습니다."
  } else if (query == ".text4") {
    content =
      "도적떼에게 쫓기다 정신을 차려보니\
    \n 당신의 눈앞에 큰 궁전이 보입니다.\
    \n\n 궁전에 들어가면 당신이 원하는 음식을\
    \n 먹을 수  있을 것처럼 보입니다.\
    \n\n 궁전에 들어가려는 순간, 갑자기 문이 말을 겁니다.\
    \n “....“"
  } else if (query == ".text5") {
    content =
      "문을 열고 들어가니\
    \n 잘 보이진  않지만, 낮익은 사람이 질문을 합니다.\
    \n\n 당신은 __ 이 먹고싶을 것입니다.\
    \n 그렇죠?"
  } else if (query == ".text6") {
    content =
        "안녕, 나는 먹키네이터야.\
      \n 거기 너, 뭐 먹고싶은지 궁금해서 온 거 맞지?\
      \n 그렇다면 저기 있는 시작 버튼을 눌러봐!"
  }

  const text = document.querySelector(query);
  let i = 0;

  function logic() {
    if (i < content.length) {
      let txt = content.charAt(i);
      text.innerHTML += txt === "\n" ? "<br/>" : txt;
      i++;
    }

  }
  setInterval(logic, 90)
}