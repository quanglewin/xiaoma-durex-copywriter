# xiaoma-durex-copywriter

**Tiếng Việt** · [English](README.md)

> Một Skill cho Claude Code / Claude.ai. Sản xuất copy và poster theo phương pháp **"hai tầng nghĩa + khoảng trắng"** của Durex thời hoàng kim trên mạng xã hội Trung Quốc (2011–2017, do agency Environment Interactive điều hành).

Thứ chuyển giao được từ phương pháp này là một cơ chế tạo ra khoảnh khắc "à, hiểu rồi". Chuyện tục chỉ là chất liệu bề mặt của ngành hàng Durex — đổi chất liệu sang khoá học AI, chuyện công sở, tài chính cá nhân hay gym, cơ chế vẫn chạy y nguyên. Đây cũng chính là bộ công thức đứng sau danh xưng mà dân marketing Việt vẫn gọi Durex: **"thánh bắt trend"**.

<p align="center">
  <img src="examples/output/lays_onechip_3x4.jpg" width="300">
  <img src="examples/output/lays_daynight_3x4.jpg" width="300">
</p>

> **Về ngôn ngữ.** Phương pháp này được xây dựng bằng tiếng Trung và kho ngữ liệu cũng là tiếng Trung. Các câu gốc được giữ nguyên tiếng Trung kèm phần diễn giải tiếng Việt, bởi vì **cái chơi chữ chính là hiện vật** — dịch nó đi thì chẳng còn gì để học. Phần giải thích viết bằng tiếng Việt, còn các ví dụ chuyển ngành được viết lại thành copy chạy được trong ngôn ngữ đích, chứ không dịch từng chữ.

---

## Hai tầng nghĩa

Một câu copy kiểu Durex đạt chuẩn phải **đứng vững đồng thời trong hai ngữ cảnh**.

| Tầng nghĩa | Nội dung |
|---|---|
| **Tầng nổi** | Bản thân trend / ngày lễ / cảnh đời thường — đọc theo nghĩa đen vẫn thông |
| **Tầng chìm** | Thương hiệu / sản phẩm / thứ bạn đang bán |

Người viết **chỉ viết tầng nổi**; tầng chìm để độc giả tự nhảy sang. Cú nhảy đó tạo ra khoái cảm, và khoái cảm đó chính là động lực lan truyền.

Ngày Ngân hàng Everbright Trung Quốc bị lỗi giao dịch, Durex đăng 「光大是不行的」— "chỉ mỗi Everbright thì không ăn thua", trong đó tên ngân hàng đọc theo nghĩa đen là "chỉ to". Khi vận động viên rào Lưu Tường ngã, Durex đặt "nhanh" cạnh "bền" và trên bề mặt chỉ nói về vận động viên. Dịp lễ Vu Lan, hãng chỉ viết năm chữ: 「今晚早回家」— "tối nay về nhà sớm".

Toàn bộ tinh thần gói trong bốn chữ: **gợi mà không phô**.

**Nói toạc ra là chết — đó là luật sắt.** Chỉ cần câu copy giải thích tầng chìm, câu đó vứt đi.

---

## Skill này làm gì

Khi được kích hoạt, skill chạy một **quy trình tương tác**, chứ không phải quăng cho bạn một bản rồi coi như xong.

```
Bước 0  Điền các ô thông tin — bằng giá trị mặc định, không phải bằng câu hỏi
        Chỉ "bán cái gì" mới đáng hỏi khi không thể suy ra;
        mọi chỗ thiếu khác đều viết thành giả định nói rõ
        "Tôi làm theo hướng 'đăng lên trang cá nhân, nhắm tới khách cũ' — sai thì bảo tôi"

Bước 1  Đưa 3–5 phương án để chọn — bắt buộc khác công thức, khác loại chủ thể, khác bảng màu
        Không được phép là ba biến thể của cùng một ý

Bước 2  Câu hỏi duy nhất — gộp "chọn phương án" và "chọn tỷ lệ" vào một lượt,
        cả hai đều cho chọn nhiều

Bước 3  Viết copy — mặc định copy ngắn, tức headline trên poster
        (≤12 ký tự Hán, ~8 từ tiếng Anh); copy dài (body copy) chỉ khi
        được yêu cầu. Trên poster luôn chỉ đặt copy ngắn

Bước 4  Ra hình — AI dựng lớp chủ thể tĩnh vật, code lo phần dàn chữ
```

> **Vì sao mặc định là không hỏi.** Mô hình có thiên hướng hỏi nhiều, mà mỗi lượt hỏi lại tiêu bớt kiên nhẫn của người dùng. Người dùng tìm bạn để lấy sản phẩm, không phải để điền khảo sát. **Một phương án cụ thể kèm giả định nói rõ có ích hơn ba câu hỏi chính xác**, bởi người dùng chỉ biết mình muốn gì khi nhìn thấy thứ cụ thể. Bản thân phương án chính là cách hỏi tốt nhất.
>
> Quy tắc này ra đời từ việc chạy eval. Vòng test đầu tiên, skill dừng lại hỏi ngay cả khi chỉ thiếu một ô, và còn tự nghĩ ra bốn câu hỏi nằm ngoài bốn ô đã định. Xem [`evals/`](evals/).

---

## Cài đặt

```bash
git clone https://github.com/crawfordxx/xiaoma-durex-copywriter.git \
  ~/.claude/skills/xiaoma-durex-copywriter
```

Có hiệu lực ở lần khởi động Claude Code kế tiếp. Cụm từ kích hoạt: "viết cho tôi ít copy", "bắt trend này", "poster ngày lễ", "nghĩ giúp câu slogan", "khoá học này quảng bá sao", "viết kiểu Durex ấy".

Phần dựng hình thì cài khi cần.

```bash
npm i @napi-rs/canvas      # dàn chữ bằng Canvas
pip install playwright     # dàn chữ bằng HTML (chọn một trong hai là đủ)
```

---

## Tám công thức copy

Phân tích đầy đủ, kèm ví dụ chuyển sang ngành không phải người lớn, nằm ở [`references/copy-formulas.vi.md`](references/copy-formulas.vi.md).

| # | Công thức | Bản gốc Durex | Chuyển sang một khoá học AI |
|---|---|---|---|
| 1 | Chơi chữ đồng âm | 「杜du饿了」(Baidu Waimai × Ele.me) | "Prompt and circumstance" |
| 2 | Chơi chữ bằng số | 「先来 7 次」("làm 7 lần trước đã") | "3 giờ bây giờ đổi lại 3 năm tăng ca" |
| 3 | Bẻ lái nghĩa | 「深耕细作」("thâm canh tỉ mỉ") | "Deep learning, shallow usage" |
| 4 | Cho đồ vật lên tiếng | "Máy giặt nói rằng…" | "Cái cốc cà phê nói: hồi trước mỗi đêm anh ấy rót đầy tôi năm lần" |
| 5 | Chiết tự | 「『日』字有多长」("chữ 日 dài bao nhiêu") | 智 = 知 + 日 — **chỉ dùng được trong tiếng Trung** |
| 6 | Câu đối / nên–kiêng | 「堵在路上 不如堵在床上」("kẹt trên giường còn hơn kẹt ngoài đường") | "Nên: bắt tay làm. Kiêng: lưu về để đó" |
| 7 | Thể thơ | Ba khổ tả cảnh + một câu hạ cánh | (chỉ dùng cho copy dài) |
| 8 | **Kiềm chế ngược** | Lễ Vu Lan: 「今晚早回家」("tối nay về nhà sớm") | "Công cụ thay thế công cụ. Nó không thay thế người đã nghĩ thông" |

Công thức 8 là đẳng cấp cao nhất: **không diễn trò đúng lúc ai cũng chờ bạn diễn trò**. Một thương hiệu bỡn cợt suốt năm bỗng nghiêm túc thì chiều sâu nhân cách được dựng lên lập tức. Không quá 5 lần mỗi năm.

---

## Hệ thống thị giác

Rút ngược ra từ **260 poster gốc**; quy chuẩn đầy đủ ở [`references/visual-system.vi.md`](references/visual-system.vi.md).

### Cây quyết định chủ thể

```
Có sản phẩm vật lý không?
├─ Có → bản thân sản phẩm có làm ẩn dụ được không?
│   ├─ Được → 【chủ thể là sản phẩm】đặt giữa, chiếm 15–35% khung hình,
│   │          nền trơn, đổ bóng mạnh
│   └─ Không → đẩy sản phẩm về góc (5–10%), nhường khung hình cho đạo cụ
└─ Không (khoá học / tri thức / dịch vụ) →
    ├─ 【chủ thể là đạo cụ】 ← hay dùng nhất, cũng hợp nhất khi không có sản phẩm
    │   ⚠️ "Không có sản phẩm vật lý" ≠ "khung hình phải trống".
    │      Đạo cụ của Durex là tĩnh vật chụp thật, có chất liệu, không phải một nét kẻ.
    └─ 【chủ thể là chữ】chữ lớn chính là hình
```

Tỷ lệ đo được: sản phẩm ~30% / **đạo cụ ~40%** / chữ ~30%. Gần như không dùng người thật; nếu có thì chỉ một bàn tay, đôi chân, hoặc bóng đổ.

### Sáu bảng màu

| Tên | Màu chính | Dùng cho |
|---|---|---|
| Đỏ thương hiệu | `#E2001A` + trắng tinh | Lễ hội, tuyên ngôn, kỷ niệm, thái độ |
| Xanh nửa đêm | `#16233F` `#0E1A2E` | Kiềm chế, sang, đêm, suy tư |
| Đen studio | `#000000` + một nguồn sáng ấm | Chất điện ảnh, hồi hộp, cận cảnh đơn sản phẩm |
| Hồng chuyển sắc | `#FCEDF1` → `#E8558F` | Valentine, hướng nữ, báo cáo cuối năm |
| Trắng ngà giấy dó | `#F1EBE0` + son `#C8102E` | Tĩnh vật, tiết khí, phong vị Trung Hoa, lịch |
| Mượn màu đối tượng | Dùng thẳng màu thương hiệu của bên kia | Collab; bắt trend phim / đội bóng / công nghệ |

### Luật sắt về dàn trang

- Copy nằm ở **1/3 trên hoặc góc trên bên trái**, căn trái; 1/3 dưới để trắng hoặc đặt chủ thể
- Cỡ chữ nội dung ≈ 3,5%–4,5% chiều rộng khung; **từ khoá phóng to 1,65–1,75 lần và tô màu thương hiệu**, phần còn lại đồng cỡ đồng màu
- Dòng eyebrow bằng 0,6 lần cỡ nội dung, màu xám, có giãn chữ
- **Logo cố định ở giữa đáy và phải nằm trên nền trống**; hình chủ thể không được đè lên
- Khoảng trắng (không gian âm) ≥ 50% khung hình. Chật = rẻ tiền

### Font chữ → [`references/typography.vi.md`](references/typography.vi.md)

**Hai điều quan trọng nhất.**

**1. Khi bắt trend (newsjacking), font chạy theo đối tượng bị bắt trend, không chạy theo thương hiệu.** Đây là phần hay bị bỏ sót nhất trong cách Durex dùng font. Nhái sự kiện iPhone thì dùng PingFang/SF; nhái poster phim thì dùng serif làm cũ kèm phụ đề viết tay; nhái CS:GO thì nhúng thẳng vào giao diện game; nhái tranh cổ động Cách mạng Văn hoá thì dùng Tống thể cũ xếp dọc. Độc giả có trí nhớ cơ bắp với những ngôn ngữ thị giác này — **font vừa hiện lên là tầng nổi đã xong**, câu copy chỉ còn lo tầng chìm.

**2. ⚠️ Vi phạm bản quyền font tiếng Trung là rủi ro pháp lý phổ biến nhất trong ấn phẩm marketing tại Trung Quốc.** Microsoft YaHei, PingFang, các bộ Founder (方正) và Hanyi (汉仪) đều cần giấy phép thương mại. **"Máy tôi có sẵn" ≠ "được dùng thương mại".** Founder và Hanyi đều có đội chuyên đi kiện, và mức đòi bồi thường cho một tấm poster thường từ vài nghìn tới vài chục nghìn tệ.

File tham chiếu liệt kê **các font thay thế miễn phí cho mục đích thương mại** thuộc tám nhóm (sans / sans đậm / serif / khải / viết tay / sans Latin / script / số & mono), kèm danh sách lằn ranh bản quyền. Không chắc thì dùng **Source Han Sans + Source Han Serif** (SIL OFL, được dùng thương mại và chỉnh sửa); tiêu đề cần lực thì dùng **Smiley Sans (得意黑)**.

---

## Vì sao không để AI viết chữ thẳng vào hình

Các mô hình sinh ảnh vẫn **làm hỏng chữ Hán — sai chữ, thiếu nét, méo tự dạng** — và làm hỏng một cách khó lường. Trong khi đó, tử huyệt của hệ thống thị giác này lại chính là **dàn chữ chính xác**.

Nên chia thành các lớp.

```
① Mô hình sinh ảnh  →  CHỈ tạo lớp tĩnh vật / chất nền;
                       prompt bắt buộc ghi NO text
② Code dàn chữ      →  gánh toàn bộ phần chữ (Canvas hoặc HTML/CSS)
③ Xuất chính xác    →  năm tỷ lệ khung hình
```

Cách này khiến chữ không bao giờ hỏng, việc tô màu từ khoá và hệ số phóng cỡ chữ vẫn kiểm soát chính xác, và **sửa copy chỉ là sửa một dòng code — ảnh tĩnh vật tái sử dụng chứ không phải sinh lại**.

Chọn hướng dàn chữ thế nào: [`references/production.vi.md`](references/production.vi.md).

| Hướng | Khi nào dùng |
|---|---|
| **Canvas** (`@napi-rs/canvas`) | Mặc định; nhất là với **mảng đồ hoạ** (ma trận icon phủ kín màn hình kiểu lịch bóc), sinh bằng code hơn hẳn xếp tay |
| **HTML/CSS + Playwright** | Bố cục phức tạp; khi muốn chỉnh theo kiểu thấy sao được vậy |
| **Satori + resvg** | Chạy hàng loạt phía server, không muốn cài trình duyệt |

---

## Ví dụ

`examples/output/` là hai poster làm bằng skill này cho Lay's — cùng một thương hiệu, hai khung bố cục hoàn toàn khác nhau.

| <img src="examples/output/lays_onechip_3x4.jpg" width="240"> | <img src="examples/output/lays_daynight_3x4.jpg" width="240"> |
|---|---|
| **「就吃一片。」** "Ăn đúng một miếng thôi."<br>Eyebrow: "lần thứ 4 nói câu này hôm nay" | **「白天数卡路里，晚上数薯片。」** "Ban ngày đếm calo, ban đêm đếm khoai tây chiên."<br>Eyebrow: A.M. 09:30 / P.M. 11:40 |
| Bẻ lái nghĩa · mảng chủ thể sản phẩm | Câu đối · chia khung ngày/đêm |

Tấm bên trái, câu copy chỉ là điều bạn tự nói với mình, bên dưới là bốn gói xếp dần từ mờ tới rõ. Nói bốn lần, tức là đã bóc bốn gói. Con "4" ở dòng eyebrow khớp với bốn gói trong hình — độc giả nhảy một cú là tới, không phải suy luận.

Tấm bên phải dùng phép đối, khung hình cắt đôi ở giữa. Nửa trên trắng lạnh là ban ngày, nửa dưới vàng tối là ban đêm, một miếng khoai rơi xuyên qua đường ranh giới — công sức của nửa ban ngày biến mất đúng theo cách đó.

Cả hai tuân thủ cùng một bộ luật cứng: copy ≤ 12 ký tự, từ khoá phóng 1,7 lần và tô đỏ thương hiệu, khoảng trắng ≥ 50%, logo cố định giữa đáy và không bị chủ thể đè. Bảng màu đều đi theo hướng **mượn màu đối tượng**, dùng chính vàng và đỏ của Lay's chứ không chọn từ sáu bảng màu. Khi làm cho một thương hiệu cụ thể, mượn màu thương hiệu luôn là lựa chọn đầu tiên.

Toàn bộ chất liệu đều là hàng thật. Bao bì là packshot chính thức từ trang của Lay's, logo lấy từ Wikimedia Commons, font dùng Source Han Sans (SIL OFL, được dùng thương mại). **Đừng tự bịa bao bì giả.**

`examples/durex-reference/` chứa 24 mẫu poster gốc của Durex ở độ phân giải thấp, dùng để đối chiếu học quy luật dàn trang (xem phần bản quyền bên dưới).

---

## Cấu trúc thư mục

```
.
├── SKILL.md                      # File chính: cơ chế, quy trình, tra nhanh công thức, lằn ranh
├── references/
│   ├── corpus.md                 # Kho ngữ liệu (34 nguồn / 260 poster)
│   ├── corpus-vn.md              # Kho Durex Việt Nam + cảnh báo gán nhầm nguồn
│   ├── copy-formulas.md          # 8 công thức chi tiết + mẫu chuyển ngành
│   ├── visual-system.md          # Quy chuẩn hệ thống thị giác đầy đủ
│   ├── typography.md             # Chọn font + lằn ranh bản quyền
│   ├── ratios.md                 # Quy chuẩn bố cục cho năm tỷ lệ
│   ├── production.md             # Pipeline ra hình và cách chọn công cụ
│   └── other-uses.md             # Các bối cảnh chuyển giao
├── evals/                        # Test case và tiêu chí (hành vi của skill đã được kiểm thử)
├── assets/
│   ├── compose_canvas.js         # Ghép hình bằng Canvas (có né vùng chữ ký)
│   ├── compose_example.py        # Ghép hình bằng HTML/Playwright
│   └── gen_hero_example.py       # Sinh ảnh tĩnh vật
└── examples/
    ├── output/                   # Thành phẩm làm bằng skill này
    └── durex-reference/          # Mẫu độ phân giải thấp của bản gốc
```

> Mỗi file trong `references/` đều có bản tiếng Việt song song `*.vi.md`. Skill khi chạy nạp bộ tiếng Anh; bộ `.vi.md` là tài liệu để đọc.

---

## Còn dùng được ở đâu nữa

Xem [`references/other-uses.vi.md`](references/other-uses.vi.md), gồm headline và ảnh bìa cho kênh cá nhân trên mạng xã hội, khoá học trả phí, SaaS B2B (bẻ lái nghĩa thuật ngữ ngành), trang chi tiết sản phẩm thương mại điện tử (cho đồ vật cạnh sản phẩm lên tiếng), tin tuyển dụng, thương hiệu cá nhân, và tài sản chuỗi theo lịch tiết khí.

File đó cũng liệt kê những bối cảnh **không chuyển giao được**, gồm ngành bị quản lý chặt, xử lý khủng hoảng truyền thông, đối tượng ít bắt sóng văn hoá mạng, và mua sắm B2B quy mô lớn.

---

## Nên làm gì và tuyệt đối không làm gì

Vụ "419 collab" năm 2017 của Durex phản tác dụng và sau đó hãng mất Environment Interactive; nguyên nhân gốc là vượt điều 3. Skill mã hoá năm điều này thành lằn ranh cứng.

1. Không đụng tới thảm hoạ, tai nạn, cái chết, bệnh tật — trừ khi đó là lập trường vì cộng đồng rõ ràng
2. Không vật hoá phụ nữ
3. **Không ám chỉ tình dục nhắm vào người thật xác định được**, và tuyệt đối không liên quan trẻ vị thành niên
4. Không bám theo nỗi đau
5. Khi chuyển sang ngành không phải người lớn, tầng chìm của câu chơi chữ phải trỏ tới **giá trị sản phẩm**, không phải một câu đùa tục

---

## Bản quyền và miễn trừ

- Các poster trong `examples/durex-reference/` **thuộc bản quyền Durex / Reckitt Benckiser**. Ở đây chỉ có 24 mẫu, nén xuống dưới 800px, phục vụ **học tập và bình luận** về phương pháp sáng tạo quảng cáo, không dùng cho bất kỳ mục đích thương mại nào.
- Kho ngữ liệu và các case được tổng hợp từ các nguồn công khai gồm Digitaling, Uisdc, Adquan, Meihua, Zhihu. **Bản quyền thuộc về tác giả gốc và nền tảng đăng tải gốc.**
- Kho mã này **không có quan hệ liên kết hay hợp tác nào** với Durex / Reckitt Benckiser.
- Nếu chủ sở hữu quyền thấy không ổn, vui lòng mở issue, nội dung sẽ được gỡ ngay.
- Phần mã nguồn (`assets/`) phát hành theo giấy phép MIT.

---

## Ghi nhận

Nguồn gốc phương pháp là **Environment Interactive** và đội của **Jin Pengyuan**, giai đoạn 2011–2017. 16.938 bài trong 6 năm, trung bình 8 bài mỗi ngày. Các công thức mọc ra từ sản lượng đó — **phải có sản lượng chất lượng cao và liên tục trước, rồi mới có công thức để đúc kết**.
