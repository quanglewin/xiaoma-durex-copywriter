# Durex Vietnam Corpus

**English** · [Tiếng Việt](corpus-vn.vi.md)

A supplement to `corpus.md` (260 Chinese lines, 2011–2017). This file collects **Vietnamese-language** copy from Durex Vietnam — same brand, same mechanism, running in a different language.

**Why this file exists**: `diction.md` says "don't copy the lines, copy the voice." But if every example is Chinese, a non-Chinese reader has no voice to copy — only glosses. A handful of real lines in a second language is worth more than two hundred read through translation. It also settles a question the Chinese corpus alone can't answer: **does the mechanism survive a change of language?** It does — but the surface tactics shift, and section 4 documents how.

---

## ⚠️ Read this first: the misattribution problem

**A great deal of "Durex content" circulating in Vietnam was never posted by Durex.**

This isn't speculation. VietnamBiz investigated and found:

- **The image riding the Jack scandal (11 Aug 2021)** — written in English, unlike Durex Vietnam's Vietnamese-language habit. Checking the official fanpage, **no matching post existed**. Conclusion: a user-made meme riding the scandal.
- **The Suez Canal / Ever Given image** — the "always protect your goods" piece that Vietnamese press called "Durex newsjacking" was actually posted by **Durex Sri Lanka's marketing team** on 27 March 2021, then spread into Vietnamese groups and was translated. **Not a Durex Vietnam post.**

Advertising Vietnam even ran a piece on the inverted phenomenon: *"Durex hadn't newsjacked yet and users had already made the memes."* Fans produce Durex-style images **before the brand can post**.

**What this means for using this corpus**: sweep up everything labeled "Durex" online and you will train on fakes — and the fakes are typically **cruder than the real thing** (memes skew vulgar; the brand has to stay inside its own limits). Learning the wrong voice fails in exactly the way that's hardest to notice.

### Confidence marks used in this file

| Mark | Meaning |
|---|---|
| ✅ | Multiple mainstream outlets, consistent with each other |
| ⚠️ | Single or weak source — study the mechanism, don't quote it as fact |
| ❌ | **Confirmed NOT Durex Vietnam** — listed so nobody adds it back |

> Note on method: Vietnamese news domains (cafef, cafebiz, vietnambiz, advertisingvietnam) are blocked from the environment this file was built in, so lines were taken from search-result summaries rather than full articles. That's why this corpus is small and marked for confidence rather than padded for volume.

---

## 1. Verified lines

### ✅ Football — goalkeeper Đặng Văn Lâm's penalty save, Vietnam topping Group G

> **「Cản phá như Lâm」** — "Block it like Lâm" (over an image of a goalkeeper's glove)
> **「Độc chiếm đỉnh G!」** — "Take sole possession of the top of G!"

Context: 2022 World Cup Asian qualifiers. Vietnam drew with Thailand and led Group G; Đặng Văn Lâm saved Thailand's penalty (19 Nov 2019).

Mechanism: **two hooks stacked in one post**.
- "Block it like Lâm" — a *proper noun* hook plus a *core action* hook: blocking is the goalkeeper's job and the product's job at once
- "Take sole possession of the top of G" — a *proper noun* hook (Group G) bent toward an anatomical reading the reader arrives at themselves

This is Durex Vietnam's best demonstration: the surface layer is entirely football, the inner layer is never stated, and the jump is exactly one hop.

### ✅ Music — riding "Mang tiền về cho mẹ" (Đen Vâu)

> **「Mang bao sung sướng về cho em hưởng」**
> "Bring home a bagful of pleasure for her to enjoy"

Context: Đen Vâu's track — "Bring the money home to mum" — dominated Vietnamese social media in late 2021; Durex posted around 13 Jan 2022.

Mechanism: **homophone substitution on a host phrase everyone already knows** — Formula 1 exactly. The "Bring X home for Y" frame stays intact; only two slots change. The reader hears the original and the rework **in the same instant**, which is the survival condition for this formula.

Worth noting: the word **bao** carries two jobs at once — a measure word ("a bagful of") and the product itself (bao = condom). Vietnamese allows this kind of stacking very naturally.

### ⚠️ Mid-Autumn Festival

> **「Sửa soạn chơi trăng, sẵn bao chờ chàng」**
> "Get ready to play under the moon; a condom waiting for him"

Mechanism: **parallelism** (Formula 6) — two six-syllable halves in tight symmetry. "Playing under the moon" is a genuine Mid-Autumn activity; the second half is the inner layer. The six-syllable meter makes it sound like folk verse, which suits a traditional festival.

### ⚠️ Valentine's Day

> A reminder not to **「va lung tung」** — "crash into things at random"

Mechanism: **homophone substitution** — "Valentine" splits into "va lung tung." One phrase carries both the holiday's name and the warning.

### ⚠️ The stoppage-time board

Durex Vietnam once made a referee's **stoppage-time board** the subject of the frame, implying extended excitement (around Aug 2021).

Mechanism: **type embedded in the subject** (see `ratios.md`) — the number appears exactly where that object normally displays information, so no explanatory word is needed. The accompanying copy could not be verified.

---

## 2. ❌ Lines that are NOT Durex Vietnam

Listed so they don't get added back later.

| Line / post | Reality |
|---|---|
| 「Hãy luôn bảo vệ hàng của bạn」 ("always protect your goods", Ever Given stuck in the Suez Canal) | Posted by **Durex Sri Lanka**, 27 Mar 2021, spread into Vietnamese groups and translated. Vietnamese press misreported it as Durex Vietnam |
| The image riding singer Jack's scandal (11 Aug 2021) | **A user-made meme.** English-language, absent from the official fanpage |

**The professional lesson underneath**: a brand that reaches the point where **the audience produces its content for it** has achieved the summit of brand personification — and simultaneously lost control of what gets attributed to it.

---

## 3. Method notes (from team interviews)

Sources: the December 2019 feature "The people behind Durex Vietnam's wildly popular Facebook posts" (syndicated across CafeBiz / VietnamNet / Soha / GenK) and Advertising Vietnam's interview with Durex Vietnam.

### ⭐ Write both outcomes before the match is played

For major matches involving Vietnam's national team, the content team **prepares two posts in advance — one for a win, one for a loss** — and publishes whichever matches the result.

This is the missing piece behind the "the window is measured in minutes" rule in `finding-the-hook.md`. Shipping in 1–9 minutes isn't a matter of thinking faster than everyone else; it's **having finished thinking before the event happened**. For any scheduled event — a match, an awards show, a product launch, an election — the outcomes are a short list. Write them all and wait.

### Real people, a real team

- The content is written by young staff in their twenties and thirties
- Agency partner: Dentsu Aegis (Siddarth Malhotra, Account Director), working to a brief of making sex more exciting
- The team reports that the company encourages creativity and pushes them to top themselves post to post

### The line they draw themselves

Durex Vietnam describes its own advertising as **"provocative and playful, but still within the bounds of Vietnamese culture."**

That's boundary 5 of `SKILL.md`'s "what to do and what never to do", stated in a local voice: suggest, don't display — and the threshold for "display" differs by market. A line that runs fine in China won't necessarily clear the bar in Vietnam, and vice versa.

---

## 4. Voice differences: Vietnamese vs Chinese

Comparing the few verified Vietnamese lines against the Chinese corpus surfaces three differences:

| | Durex China (2011–2017) | Durex Vietnam |
|---|---|---|
| Length | Median 6 characters; many lines of 2–4 (「上车～」) | Longer — usually a complete 5–8 syllable clause; rarely clipped |
| Rhythm | Cut by punctuation (`～` `。` `——`) | Cut by **rhyme and symmetry** — "chơi trăng / chờ chàng", "Cản phá như Lâm" |
| Pun material | Chinese homophones, character decomposition, numbers | **Universally known phrases** (song lyrics, idioms), spoonerisms (nói lái), measure-word stacking |

**The takeaway for writing in any non-Chinese language**: don't force lines down to four words to match the Chinese median. The median was a measurement of Chinese, not a law of the method. Vietnamese draws its force from **rhyme and parallel structure**, not from terseness — "Sửa soạn chơi trăng, sẵn bao chờ chàng" is twice the length of 「上车～」 and holds up fine, because the meter is itself a structure.

The rule that does survive translation is the one that was never about length: **one hop, and never explain it.**

---

## 5. Durex global (English) — different genre, for reference only

⚠️ **This is not a daily newsjacking operation.** Durex global works mainly in **taglines and print advertising**, a different genre from Durex China's 8-posts-a-day cadence or Durex Vietnam's newsjacking. Don't use this section as a model for social copy.

Documented official taglines:
- **"Love Sex"** — the same small line that sits above the logo in the poster lockup described in `visual-system.md`
- **"Fit Matters"** — for the size-based product range

Notable campaigns: **"Let's lube"** (confronting the misrepresentation of women's sexual experience) and a campaign **reclaiming the word "moist"**, one of the most disliked words in English.

> ⚠️ **Source warning**: most "Durex slogans" floating around slogan-aggregator sites (sloganlist, logotaglines, and similar) are **wrong or invented**. Do not copy from them into this corpus. Only accept lines traceable to a real campaign.

---

## 6. Copyright

All copy quoted in this file is **copyright Durex / Reckitt Benckiser**, quoted minimally for **study and commentary** on advertising creative method. Context and analysis are compiled from the public sources cited below; article copyright remains with the original authors and publications. This repository has no affiliation with Durex / Reckitt Benckiser.

## Sources

- VietnamBiz — [The origin of the Durex "newsjacking" image of the ship stuck in the Suez Canal](https://vietnambiz.vn/nguon-goc-buc-hinh-durex-bat-trend-tau-cho-hang-mac-ket-tai-kenh-suez-20210329173202718.htm)
- VietnamBiz — [Social media raves about Durex's divine newsjacking — but is that accurate?](https://vietnambiz.vn/mxh-ran-ran-tan-thuong-kha-nang-bat-trend-than-thanh-cua-durex-nhung-lieu-dieu-do-co-dung-20210812131803293.htm)
- Advertising Vietnam — [Durex hadn't newsjacked yet and users had already made the memes](https://advertisingvietnam.com/durex-chua-bat-trend-ma-nguoi-dung-da-nhanh-tay-che-anh-bi-quyet-tao-user-generated-content-p17427)
- Advertising Vietnam — [Durex Vietnam: "Our advertising is provocative and playful, but within the bounds of Vietnamese culture"](https://advertisingvietnam.com/article/durex-viet-nam-quang-cao-cua-chung-toi-khieu-khich-tinh-nghich-nhung-van-trong-khuon-kho-van-hoa-viet-l17340)
- CafeBiz — [The people behind Durex Vietnam's wildly popular Facebook posts](https://cafebiz.vn/nhung-guong-mat-dung-sau-cac-bai-viet-van-nguoi-me-tren-facebook-cua-durex-viet-nam-20191201094700625.chn)
- CafeF — [Durex rides the "Mang tiền về cho mẹ" trend](https://cafef.vn/den-hen-lai-len-durex-bat-trend-mang-tien-ve-cho-me-choi-chu-chat-nhu-nuoc-cat-man-so-2-kho-ai-so-1-20220113142332687.chn)
- CafeF — [Durex turns the stoppage-time board into the subject of the frame](https://cafef.vn/lam-marketing-man-nhu-durex-bien-bang-bu-gio-thanh-ba-con-soi-khong-lo-ngu-y-keo-dai-thoi-gian-hung-phan-20210818140636461.chn)
- Campaign — [Durex advertising and campaigns](https://www.campaignlive.co.uk/the-work/advertiser/durex/10303)
