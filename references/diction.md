# Wording and Voice

`copy-formulas.md` governs **structure**. This file governs **wording**.

Right structure with AI-voice wording still reads fake on sight. **The formula makes the line work; the diction makes it sound like a person wrote it.**

Every pattern here was tabulated backwards from the 260+ real lines in `corpus.md`. None of it is by feel.

> **On language**: the length rules were measured in Chinese characters. The English working equivalent is given alongside — roughly one Chinese character ≈ 0.6 English words, so 12 characters ≈ 7–8 words.

---

## 1. Sentence Length: Median 6 Characters

Measured distribution:

| Characters | Original lines |
|---|---|
| 2–4 | 上车～ ("get in")　今晚！ ("tonight!")　开学日。 ("back to school.")　且可闹～ ("let's make a racket")　今日吉时 ("today's auspicious hour")　预备—— ("on your marks——")　Oh!　Red now |
| 5–8 | 我就蹭蹭 ("just the tip")　安全，第一 ("safety, first")　今晚早回家 ("come home early tonight")　你吃了吗？ ("have you eaten?")　光大是不行的 ("Everbright alone won't do it")　一杜之遥 ("a Durex away")　昼伏夜入 ("lie low by day, enter by night")　别乱跑 ("don't wander off") |
| 9–12 | 今晚，好戏上演…… ("tonight, the real show begins…")　真正的司机，重视每一次安全 ("a real driver takes every safety measure seriously")　堵在路上 不如堵在床上 ("better stuck in bed than in traffic") |
| 12+ | **Rare**, and always parallel or serial in structure |

**Past 12 characters (≈8 English words) without parallelism, you've simply written long.** Cut it to under 8 characters and look again — it's usually better.

### ⚠️ But the median is a measurement, not a target

Durex also wrote 「北京今日暴雨，幸亏包里还有两只杜蕾斯」(17 characters) and 「最快的男人并不是最好的，坚持到底才是真正强大的男人」(25 characters) — two of its most famous lines.

**Short is what happens once the thing is said and the sentence stops on its own. It is not a length you decide first and then stuff words into.**

Cutting the metaphor to hit a length turns the pun into a riddle: the reader can't make the jump, and the line is just as dead. The order is always **guarantee the one-hop jump first, then see whether it can get shorter**.

---

## 2. Punctuation Is Tone, Not Grammar

This is what AI most often drops, and the fastest tell that a human wrote it.

| Mark | Function | Original lines |
|---|---|---|
| `～` | Flippant, a little tug | 上车～　且可闹～　十一，放开玩～　两个人 wow～ |
| `。` after a fragment | Flat, final, no discussion | 开学日。　我们，卧室见。　Good Shot. |
| `！` | Sudden force | 今晚！　爱劳动，最光荣！　其实人类早就输给机器了！！ |
| `——` | Held, the sentence swallowed | 预备—— |
| `？` | Asking what it already knows | 你吃了吗？　小满？小小的就能满足？　结束了吗？ |
| `……` | Left for you to finish | 今晚，好戏上演…… |
| `?!` `:)` | Internet register | This is 7 ?!　拿去骗那些没戴杜蕾斯的吧 :) |

**Commas cut rhythm; they don't join clauses.** The comma in 「安全，第一」("safety, first") is a beat, not a list.

In English the same instincts apply: a period after a fragment, an em dash that holds instead of explaining, no semicolons.

---

## 3. Verbs First, Adjectives Near Zero

High-frequency verbs in the real corpus: **蹭 (rub), 上 (get on/mount), 来 (come), 进 (enter), 堵 (block), 挤 (squeeze), 奔赴 (rush to), 撤出 (withdraw), 通行 (pass through), 回家 (go home), 乱跑 (wander), 抱 (hold), 点燃 (ignite), 放开 (let go)**

Almost never appear anywhere in the corpus: ultimate, deep, all-new, professional, premium, outstanding, meticulous, artisanal, empower, craft, boost, unlock, embark.

> 「上车～」("get in") — one verb is enough.
> The AI version writes "let us embark together on this beautiful journey."

**When you catch yourself writing an adjective, first try swapping it for a verb.**

---

## 4. Stuff Words into Existing Idioms; Don't Invent New Ones

| Altered | Host phrase |
|---|---|
| 震震日上 | 蒸蒸日上 ("rising steadily") |
| 万湿如意 | 万事如意 ("may all things go as you wish") |
| 梅开五杜 | 梅开二度 ("scoring twice") |
| 且行且安全 | 且行且珍惜 ("cherish it as you go") |
| 李所 ying 得 | 理所应得 ("only right and proper") |
| 五「次」青年节 | 五四青年节 ("May Fourth Youth Day") |

Two hard rules:

1. **The host phrase has to be universally known** — the reader must hear the original in the same instant they hear the new one. If they can't hear it, the line doesn't exist
2. **Change only 1–2 characters** (in English: one or two syllables). Change more and it becomes a different phrase, and the jump is gone

Inventing a coinage nobody has ever heard is the single most typical AI failure mode.

English works the same way — "Prompt and circumstance", "Adapt or AI", "The road not prompted" all lean on a host phrase the reader already carries.

---

## 5. Person: Mostly "You"; "I" Is for Personification

- **You** (most frequent): 你负责横冲直撞 ("you charge ahead")　你吃了吗 ("have you eaten")　别乱跑 ("don't wander off")　希望你过得好 ("I hope you do well")
- **I / we** (personification, close-up): 我就蹭蹭 ("just the tip")　我们，卧室见。 ("see you in the bedroom.")　我为你保驾护航 ("I'll ride escort for you")
- **The object speaking as itself** (scene transplant only): the washing machine says "the intensity of that love beats anything I manage on spin cycle"

**Almost never used**: users, everyone, folks, friends, each and every one of us.

The moment "everyone" appears the human is gone — that's the register of an announcement, not of talking to someone.

---

## 6. Never Explain Yourself ⚠️

Across all 260+ lines, these expressions appear **zero times**:

> which means　what it really is　in other words　the logic behind it is　the reason … is because　that's the power of …　and that right there is …

"Explain it and it dies" governs more than the inner meaning — **it governs the effect too.** Durex never tells you how clever it just was.

This is the hardest habit for a model to break: it wants to complete the thought, wants you to confirm it understood. **Hold it. Write the line and stop.**

---

## 7. English Copy: ≤4 Words, Ending in a Period

Good Shot.　Love And Peace.　Left is right.　Real Men, Real Madrid.　LIGHT OFF SHOW ON　Everybody OK!　Red now

The pattern: **short, periods rather than exclamation marks, initial capitals**. No full sentences, no subordinate clauses.

When the whole line is in English, this is the ceiling — not "under 12 characters."

---

## 8. Numbers Are Used as Words, with No Quantifiers Attached

001 点　先来 7 次　一日等于 24 小时　A.M. 04：00　Happy 1G24 Day　反复听了 69 次　520 小时

The number is the pun's vehicle by itself. **Don't prop it up with "as many as," "up to," or "a full."**

---

## 9. The AI-Voice Comparison Table

Run this over the finished draft. On the left is the model's default output; on the right, the original.

| AI writes | The original |
|---|---|
| Let us embark together on a beautiful journey | 上车～ ("get in") |
| Safety has always been our top priority | 安全，第一 ("safety, first") |
| Wishing you and your family a joyous Mid-Autumn reunion | 吃了吗？ ("eaten yet?") |
| On this special day, we would like to say to you | 今晚！ ("tonight!") |
| A new term has begun; let us work hard together | 开学日。 ("back to school.") |
| An ultra-thin, skin-hugging product experience | 见之不显，隐薄于空 ("seen but not apparent, thin to the point of air") |
| Amid the busyness, remember to head home and be with family | 今晚早回家 ("come home early tonight") |
| Through deep insight into user needs, empowering you with an all-new experience | (no sentence of this kind exists anywhere in the corpus) |

**The shared symptom**: saying all of it, naming the emotion, listing every benefit.

Durex does the opposite — **say half, and let the reader walk the other half.** Finishing that walk is the reason they share it.

---

## 10. Final Draft Checklist (6 items)

- [ ] Is the headline within 12 Chinese characters (≈8 English words)? If over, is it parallel in structure?
- [ ] Is any punctuation mark carrying tone? (All well-behaved periods = no tone)
- [ ] Can the adjectives become verbs?
- [ ] Does it explain itself? (If "actually", "which means", "that's the power of" appears → delete)
- [ ] Is the person "you" or "everyone"?
- [ ] Read it aloud. Does it sound like one person talking to another? If not, rewrite.
