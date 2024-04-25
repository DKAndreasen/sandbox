# Results from the tuning/testing script
Manually copy-pasted into here.

mean F1 score is based on the F1 BERTScore between 711 question/answer pairs. With questions asked by frontworkers and answered or verified by domain specialists.

The confused scores are based on 10 datasets where the answers to questions have been shuffled randomly.

An example of a question/answer pair is:
> Q: "hvorfor skal der dispenseres på alle ordinationer før man kan få godkendt en dispensering? eksempel hvis en borger har nitroglycering som PN spray, den kan af gode grunde ikke doseres, men for at få doseringen til at gå igennem, så skal jeg trykke den som dispenseret. Kan det passe?"
> 
> A: "Ja, det kan det godt. Når du vinger af ved PN-præparater, så tager du stilling til, at der er medicin nok til næste gang, der skal dispenseres."

and an answer for another question could then serve as a confused answer for this question, this could be:
> cA: "Hvis der er tilknyttet en bemærkning til ydelsen kan det ses ved at dobbeltklikke på ydelsen."

## Model: KennethTM/bert-base-uncased-danish
Danish bert model with _danish tokenizer_

### without IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.5087 | 0.5358 | 0.5674 | 0.5798 | 0.5810 | 0.6067 | 0.6073 | 0.6207 | 0.6559 | 0.6709 | 0.7162 | **0.7865** | 0.7154 |
| mean confused F1 score | 0.4176 | 0.4482 | 0.4897 | 0.5120 | 0.5210 | 0.5549 | 0.5603 | 0.5763 | 0.6171 | 0.6339 | 0.6816 | **0.7576** | 0.6736 |
| *mean offsetted F1 score* | **0.0912** | 0.0876 | 0.0777 | 0.0678 | 0.0600 | 0.0518 | 0.0470 | 0.0444 | 0.0388 | 0.0370 | 0.0346 | 0.0289 | 0.0419 |

### with IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4019 | 0.4552 | 0.5022 | 0.5306 | 0.5446 | 0.5782 | 0.5894 | 0.6067 | 0.6446 | 0.6707 | 0.7179 | **0.7847** | 0.7035 |
| mean confused F1 score | 0.2785 | 0.3363 | 0.3969 | 0.4396 | 0.4654 | 0.5105 | 0.5292 | 0.5497 | 0.5953 | 0.6251 | 0.6755 | **0.7488** | 0.6500 |
| *mean offsetted F1 score* | **0.1234** | 0.1189 | 0.1053 | 0.0910 | 0.0792 | 0.0677 | 0.0602 | 0.0570 | 0.0494 | 0.0456 | 0.0424 | 0.0358 | 0.0535 |

## Model: bert-base-multilingual-cased
The multilingual model that BERTScore suggest for other languages (ie. also Danish)

### without IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4880 | 0.5515 | 0.5457 | 0.5907 | 0.6197 | 0.6756 | 0.7118 | 0.6258 | 0.5990 | 0.6678 | 0.7256 | **0.7607** | 0.5470 |
| mean confused F1 score | 0.3776 | 0.4535 | 0.4506 | 0.5071 | 0.5474 | 0.6197 | 0.6692 | 0.5742 | 0.5475 | 0.6252 | 0.6891 | **0.7256** | 0.4705 |
| *mean offsetted F1 score* | **0.1104** | 0.0980 | 0.0951 | 0.0836 | 0.0723 | 0.0560 | 0.0426 | 0.0516 | 0.0515 | 0.0426 | 0.0365 | 0.0351 | 0.0764 |

### with IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4078 | 0.4809 | 0.4859 | 0.5419 | 0.5850 | 0.6510 | 0.6982 | 0.6133 | 0.5877 | 0.6566 | 0.7176 | **0.7524** | 0.5275 |
| mean confused F1 score | 0.2744 | 0.3615 | 0.3712 | 0.4414 | 0.4985 | 0.5843 | 0.6479 | 0.5530 | 0.5281 | 0.6072 | 0.6753 | **0.7116** | 0.4382 |
| *mean offsetted F1 score* | **0.1335** | 0.1193 | 0.1146 | 0.1005 | 0.0866 | 0.0667 | 0.0502 | 0.0603 | 0.0596 | 0.0494 | 0.0423 | 0.0409 | 0.0893 |

## Model: AI-Sweden-Models/roberta-large-1160k
Listed as SOTA at [:hug:/danish-foundation-models](https://huggingface.co/danish-foundation-models)

### without IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 | layer 14 | layer 15 | layer 16 | layer 17 | layer 18 | layer 19 | layer 20 | layer 21 | layer 22 | layer 23 | layer 24 | layer 25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4849 | 0.7280 | 0.8094 | 0.8126 | 0.7866 | 0.7808 | 0.7966 | 0.8289 | 0.8493 | 0.8556 | 0.8635 | 0.8609 | 0.8602 | 0.8586 | 0.8670 | 0.8675 | 0.8670 | 0.8670 | 0.8626 | 0.8712 | 0.8800 | 0.8898 | 0.9028 | **0.9075** | 0.5785 |
| mean confused F1 score | 0.4052 | 0.6816 | 0.7781 | 0.7836 | 0.7551 | 0.7471 | 0.7644 | 0.8031 | 0.8270 | 0.8349 | 0.8427 | 0.8405 | 0.8397 | 0.8403 | 0.8512 | 0.8460 | 0.8452 | 0.8458 | 0.8407 | 0.8498 | 0.8601 | 0.8708 | 0.8862 | **0.8923** | 0.5080 |
| *mean offsetted F1 score* | **0.0797** | 0.0463 | 0.0313 | 0.0290 | 0.0314 | 0.0338 | 0.0322 | 0.0258 | 0.0223 | 0.0207 | 0.0208 | 0.0204 | 0.0205 | 0.0184 | 0.0159 | 0.0215 | 0.0218 | 0.0212 | 0.0219 | 0.0214 | 0.0200 | 0.0190 | 0.0166 | 0.0152 | 0.0705 |

### with IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 | layer 14 | layer 15 | layer 16 | layer 17 | layer 18 | layer 19 | layer 20 | layer 21 | layer 22 | layer 23 | layer 24 | layer 25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4017 | 0.6440 | 0.7572 | 0.7747 | 0.7574 | 0.7508 | 0.7664 | 0.8069 | 0.8326 | 0.8405 | 0.8511 | 0.8484 | 0.8485 | 0.8505 | 0.8593 | 0.8611 | 0.8621 | 0.8624 | 0.8560 | 0.8623 | 0.8707 | 0.8795 | 0.8912 | **0.8966** | 0.5386 |
| mean confused F1 score | 0.3044 | 0.5826 | 0.7161 | 0.7373 | 0.7174 | 0.7072 | 0.7242 | 0.7732 | 0.8039 | 0.8139 | 0.8247 | 0.8224 | 0.8225 | 0.8276 | 0.8392 | 0.8343 | 0.8352 | 0.8363 | 0.8289 | 0.8358 | 0.8461 | 0.8559 | 0.8703 | **0.8776** | 0.4527 |
| *mean offsetted F1 score* | **0.0973** | 0.0614 | 0.0411 | 0.0374 | 0.0399 | 0.0436 | 0.0422 | 0.0338 | 0.0287 | 0.0266 | 0.0264 | 0.0260 | 0.0259 | 0.0229 | 0.0201 | 0.0268 | 0.0269 | 0.0261 | 0.0271 | 0.0266 | 0.0246 | 0.0236 | 0.0209 | 0.0189 | 0.0859 |

## Model: KennethEnevoldsen/dfm-sentence-encoder-large-exp1
At the top of [scandeval.com/danish-nlu](https://scandeval.com/danish-nlu/)

### without IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 | layer 14 | layer 15 | layer 16 | layer 17 | layer 18 | layer 19 | layer 20 | layer 21 | layer 22 | layer 23 | layer 24 | layer 25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4724 | 0.4995 | 0.4861 | 0.4558 | 0.4431 | 0.4394 | 0.4244 | 0.4426 | 0.4646 | 0.4569 | 0.4653 | 0.4560 | 0.4447 | 0.4547 | 0.4673 | 0.5006 | 0.5322 | 0.5517 | 0.5726 | 0.5959 | 0.6249 | 0.6593 | 0.6747 | **0.6863** | 0.5522 |
| mean confused F1 score | 0.3670 | 0.3943 | 0.3825 | 0.3521 | 0.3379 | 0.3301 | 0.3130 | 0.3315 | 0.3570 | 0.3542 | 0.3668 | 0.3623 | 0.3510 | 0.3607 | 0.3781 | 0.4139 | 0.4482 | 0.4698 | 0.4902 | 0.5106 | 0.5320 | 0.5642 | **0.5797** | 0.5789 | 0.3851 |
| *mean offsetted F1 score* | 0.1054 | 0.1052 | 0.1036 | 0.1037 | 0.1052 | 0.1093 | 0.1114 | 0.1110 | 0.1076 | 0.1027 | 0.0986 | 0.0938 | 0.0937 | 0.0939 | 0.0892 | 0.0867 | 0.0839 | 0.0819 | 0.0823 | 0.0852 | 0.0929 | 0.0951 | 0.0951 | 0.1074 | **0.1670** |


### with IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 | layer 14 | layer 15 | layer 16 | layer 17 | layer 18 | layer 19 | layer 20 | layer 21 | layer 22 | layer 23 | layer 24 | layer 25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.3833 | 0.4159 | 0.4220 | 0.3986 | 0.3934 | 0.3936 | 0.3910 | 0.4091 | 0.4282 | 0.4233 | 0.4348 | 0.4300 | 0.4179 | 0.4268 | 0.4378 | 0.4689 | 0.4995 | 0.5175 | 0.5383 | 0.5640 | 0.5948 | 0.6328 | 0.6489 | **0.6622** | 0.5548 |
| mean confused F1 score | 0.2463 | 0.2779 | 0.2878 | 0.2657 | 0.2585 | 0.2528 | 0.2482 | 0.2671 | 0.2902 | 0.2924 | 0.3091 | 0.3106 | 0.2993 | 0.3092 | 0.3245 | 0.3567 | 0.3903 | 0.4103 | 0.4302 | 0.4535 | 0.4773 | 0.5154 | 0.5324 | **0.5360** | 0.3787 |
| *mean offsetted F1 score* | 0.1370 | 0.1380 | 0.1342 | 0.1329 | 0.1348 | 0.1408 | 0.1427 | 0.1420 | 0.1380 | 0.1309 | 0.1257 | 0.1193 | 0.1186 | 0.1176 | 0.1133 | 0.1122 | 0.1092 | 0.1072 | 0.1081 | 0.1105 | 0.1175 | 0.1174 | 0.1166 | 0.1263 | **0.1761** |

## Model: KennethEnevoldsen/dacy-large-encoder

### without IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 | layer 14 | layer 15 | layer 16 | layer 17 | layer 18 | layer 19 | layer 20 | layer 21 | layer 22 | layer 23 | layer 24 | layer 25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.4852 | 0.5013 | 0.4901 | 0.4614 | 0.4481 | 0.4509 | 0.4381 | 0.4496 | 0.4780 | 0.4703 | 0.4829 | 0.4670 | 0.4300 | 0.4401 | 0.4396 | 0.4432 | 0.4773 | 0.4835 | 0.5035 | 0.5333 | 0.5546 | 0.5788 | 0.5784 | **0.5922** | 0.5840 |
| mean confused F1 score | 0.3808 | 0.3956 | 0.3885 | 0.3611 | 0.3480 | 0.3488 | 0.3361 | 0.3505 | 0.3862 | 0.3864 | 0.4060 | 0.3975 | 0.3620 | 0.3742 | 0.3799 | 0.3853 | 0.4233 | 0.4303 | 0.4507 | 0.4800 | 0.5019 | 0.5291 | 0.5288 | **0.5444** | 0.5372 |
| *mean offsetted F1 score* | 0.1044 | **0.1057** | 0.1016 | 0.1003 | 0.1002 | 0.1021 | 0.1020 | 0.0992 | 0.0918 | 0.0839 | 0.0770 | 0.0696 | 0.0680 | 0.0659 | 0.0597 | 0.0579 | 0.0539 | 0.0532 | 0.0529 | 0.0533 | 0.0527 | 0.0496 | 0.0496 | 0.0478 | 0.0467 |


### with IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 | layer 14 | layer 15 | layer 16 | layer 17 | layer 18 | layer 19 | layer 20 | layer 21 | layer 22 | layer 23 | layer 24 | layer 25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.3949 | 0.4193 | 0.4294 | 0.4085 | 0.4024 | 0.4088 | 0.4051 | 0.4175 | 0.4450 | 0.4430 | 0.4580 | 0.4486 | 0.4221 | 0.4313 | 0.4281 | 0.4300 | 0.4610 | 0.4604 | 0.4728 | 0.4991 | 0.5210 | 0.5479 | 0.5443 | **0.5577** | 0.5480 |
| mean confused F1 score | 0.2594 | 0.2815 | 0.2985 | 0.2801 | 0.2743 | 0.2783 | 0.2757 | 0.2921 | 0.3289 | 0.3383 | 0.3622 | 0.3635 | 0.3405 | 0.3529 | 0.3574 | 0.3616 | 0.3973 | 0.3972 | 0.4100 | 0.4360 | 0.4590 | 0.4899 | 0.4864 | **0.5020** | 0.4938 |
| *mean offsetted F1 score* | 0.1355 | **0.1378** | 0.1309 | 0.1284 | 0.1282 | 0.1305 | 0.1293 | 0.1253 | 0.1160 | 0.1047 | 0.0958 | 0.0851 | 0.0816 | 0.0784 | 0.0707 | 0.0684 | 0.0637 | 0.0632 | 0.0628 | 0.0631 | 0.0620 | 0.0581 | 0.0578 | 0.0557 | 0.0542 |

## Model: google/mt5-base
The model Laura and Malte uses

### without IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.5535 | 0.7167 | 0.7220 | 0.7561 | 0.8041 | 0.8133 | 0.8132 | 0.8054 | 0.8117 | **0.8373** | 0.8347 | 0.8296 | 0.5539 |
| mean confused F1 score | 0.4612 | 0.6581 | 0.6683 | 0.7150 | 0.7739 | 0.7865 | 0.7875 | 0.7798 | 0.7873 | **0.8170** | 0.8154 | 0.8101 | 0.5029 |
| *mean offsetted F1 score* | **0.0923** | 0.0586 | 0.0537 | 0.0410 | 0.0302 | 0.0268 | 0.0258 | 0.0256 | 0.0243 | 0.0203 | 0.0193 | 0.0195 | 0.0510 |

### with IDF offset
|     | layer 1 | layer 2 | layer 3 | layer 4 | layer 5 | layer 6 | layer 7 | layer 8 | layer 9 | layer 10 | layer 11 | layer 12 | layer 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean F1 score | 0.3822 | 0.6089 | 0.6265 | 0.6944 | 0.7575 | 0.7725 | 0.7739 | 0.7661 | 0.7744 | **0.8088** | 0.8070 | 0.7998 | 0.4730 |
| mean confused F1 score | 0.2496 | 0.5219 | 0.5469 | 0.6354 | 0.7138 | 0.7340 | 0.7367 | 0.7294 | 0.7394 | **0.7798** | 0.7795 | 0.7722 | 0.4000 |
| *mean offsetted F1 score* | **0.1326** | 0.0871 | 0.0796 | 0.0590 | 0.0437 | 0.0385 | 0.0372 | 0.0367 | 0.0350 | 0.0291 | 0.0275 | 0.0276 | 0.0730 |
