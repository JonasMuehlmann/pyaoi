# Changelog

<!--next-version-placeholder-->

## v2.5.0 (2021-04-20)
### Feature
* Implement `rotate_copy()`, `shift_left()` and `shift_right()` ([`69d116c`](https://github.com/JonasMuehlmann/pyaoi/commit/69d116cf5d5bd2f15d15a4b7927dd5648b172df9))

### Documentation
* Update Readme.md ([`d380ebc`](https://github.com/JonasMuehlmann/pyaoi/commit/d380ebc78fb4a617590a9cb551af05b2b1a94e40))

## v2.4.0 (2020-12-31)
### Feature
* Implement transform_n() ([`168a99a`](https://github.com/JonasMuehlmann/pyaoi/commit/168a99a10291357be815c34ed37146f9733949f9))
* Implement transform() ([`45ba99b`](https://github.com/JonasMuehlmann/pyaoi/commit/45ba99b945926eee6491d3f07becced5d06c2ebe))

## v2.3.0 (2020-12-31)
### Feature
* Implement fill_n() ([`606a1b1`](https://github.com/JonasMuehlmann/pyaoi/commit/606a1b13ad3bb4fce0509ec128bc4057937898e8))
* Implement fill() ([`9fb3d16`](https://github.com/JonasMuehlmann/pyaoi/commit/9fb3d16c0669fe18de301c2a5a54213fcbc41dd2))

## v2.2.0 (2020-12-31)
### Feature
* Implement copy_except_if_not() ([`83678ff`](https://github.com/JonasMuehlmann/pyaoi/commit/83678ff784990693c5e0137624d3b7da36209aaf))
* Implement copy_except_if() ([`f7dd1eb`](https://github.com/JonasMuehlmann/pyaoi/commit/f7dd1eb0e710902ad7b5f7c6a07f3c4c55f1d16b))
* Implement copy_except() ([`a5e2102`](https://github.com/JonasMuehlmann/pyaoi/commit/a5e2102e2d83d60eb4fb4d4a2f3f5dcb78a51ef3))

## v2.1.0 (2020-12-30)
### Feature
* Implement copy_replace_if_not() ([`f16d338`](https://github.com/JonasMuehlmann/pyaoi/commit/f16d338e419ebeb52b149dd2cd72e425ac41727a))
* Implement copy_replace_if() ([`252c8b5`](https://github.com/JonasMuehlmann/pyaoi/commit/252c8b5db1aa83c5c343576b534018469fb457e2))
* Implement copy_replace() ([`eeab885`](https://github.com/JonasMuehlmann/pyaoi/commit/eeab885ed7f469c292e007d470abae4b4ae3bafa))

## v2.0.0 (2020-12-30)
### Breaking
* Function search_n() now returns -1 when being passed     an emtpy sequence or there are no num_elements repetitions of     parameter value  ([`2c1ea28`](https://github.com/JonasMuehlmann/pyaoi/commit/2c1ea28559512291eef1b8afb422082014f78c11))
* Function search() now returns -1 when being passed at     least one empty sequence or sequence_sub does not occur once in     sequence_super  ([`1346efb`](https://github.com/JonasMuehlmann/pyaoi/commit/1346efb32c66eda2e4e33d6fe9ff24186c494d34))
* Function adjacent_find() now returns -1 if no two     adjacent elements are considered equal  ([`5c5f2bf`](https://github.com/JonasMuehlmann/pyaoi/commit/5c5f2bfd24a06ab81283e85b1ca0af7305959f51))
* Parameters values_in and values_from of function     find_first_of() have been renamed to iterable_super and interable_sub BREAKING CHANGE: Function find_first_of() now returns -1 if it is     being passed at least one empty iterable or iterable:_sub does not     occur once in iterable_super  ([`d62f734`](https://github.com/JonasMuehlmann/pyaoi/commit/d62f734fd30560d2e13ebcd1eb924fa52b5ccd2e))
* Function find_end() now returns -1 if it is being     passed at least one empty collection or collection_sub does not     occur once in collection_super  ([`84454ba`](https://github.com/JonasMuehlmann/pyaoi/commit/84454baee9398a237baab1dcbff06380fb8217e8))
* Functions find(), find_if() and find_if_not() now     return -1 when they are being passed empty iterables BREAKING CHANGE: Parameter collection of functions find_if() and find_if_not() has been renamed to iterable and it's type hind has been     changed accordingly  ([`154eef7`](https://github.com/JonasMuehlmann/pyaoi/commit/154eef73e155d81763d7d0b4181ec3c60fd405b3))
* Function mismatch() now correctly returns None if     both sequences do not differ  ([`5938083`](https://github.com/JonasMuehlmann/pyaoi/commit/5938083fb85cecf52a2a6221da3d6973785f7d42))
* Parameter iterable of function count_if_not() has     been renamed to collection, it's type hint/requirement has changed     accordingly ([`6af8983`](https://github.com/JonasMuehlmann/pyaoi/commit/6af89835e47a86c606fa6c0e5323424d04142428))
* Function count_if_not() returns 0, instead of -1,     when being passed an empty collection  ([`6af8983`](https://github.com/JonasMuehlmann/pyaoi/commit/6af89835e47a86c606fa6c0e5323424d04142428))
* Parameter readonly of functions for_each() and     for_each_n() has been removed, they are not allowed to modify     their passed in iterable  ([`ecfd728`](https://github.com/JonasMuehlmann/pyaoi/commit/ecfd728eb46e0a63314b0d450d9516675a12c87c))

## v1.0.0 (2020-12-28)
### Breaking
* Parameter n of functions for_each_n() has been renamed to num_elements ([`c788046`](https://github.com/JonasMuehlmann/pyaoi/commit/c788046bfa057609c58d6e39d1e0ba8b11cc23bb))
* Parameters iterable1 and iterable2 of function mismatch() has been renamed to sequence1 and sequence2 ([`c788046`](https://github.com/JonasMuehlmann/pyaoi/commit/c788046bfa057609c58d6e39d1e0ba8b11cc23bb))
* Parameter collection of function adjacent_find() has been renamed to sequence ([`c788046`](https://github.com/JonasMuehlmann/pyaoi/commit/c788046bfa057609c58d6e39d1e0ba8b11cc23bb))
* Parameters collection_super and collection_sub of function search() have been renamed to sequence_super and sequence_sub ([`c788046`](https://github.com/JonasMuehlmann/pyaoi/commit/c788046bfa057609c58d6e39d1e0ba8b11cc23bb))
* Parameter sequence of function search_n() has been renamed to sequence ([`c788046`](https://github.com/JonasMuehlmann/pyaoi/commit/c788046bfa057609c58d6e39d1e0ba8b11cc23bb))
* Parameter n of function search_n() has been renamed to num_elements  ([`c788046`](https://github.com/JonasMuehlmann/pyaoi/commit/c788046bfa057609c58d6e39d1e0ba8b11cc23bb))

### Documentation
* Add instructions to CONTRIBUTING.md ([`051a6c2`](https://github.com/JonasMuehlmann/pyaoi/commit/051a6c2eea10a9337b71e9d7f44bc5d7026bc82d))
* Add extra instructions to CONTRIBUTING.md ([`dce131b`](https://github.com/JonasMuehlmann/pyaoi/commit/dce131ba2bde57bbb1fcb8874ea4e633214a4e32))

## v0.1.0 (2020-12-26)
### Feature
* Implement search() and search_n() ([`e3a3fdb`](https://github.com/JonasMuehlmann/pyaoi/commit/e3a3fdbc1bb2d75bad704d78fcbf51843d88b339))

### Fix
* Correct config section so python-semantic-release can find it ([`8c53492`](https://github.com/JonasMuehlmann/pyaoi/commit/8c53492af651f5507201a540bda080edcabdc736))
* Correct file path ([`c70823a`](https://github.com/JonasMuehlmann/pyaoi/commit/c70823a220642cff4c87c135c18bf5e2bde80908))
* Correct bad merge after refactor and implementation change ([`d283df4`](https://github.com/JonasMuehlmann/pyaoi/commit/d283df47393af02171ca8947d2dea6f59ab5d5ba))
* Corrected syntax ([`3fb37c1`](https://github.com/JonasMuehlmann/pyaoi/commit/3fb37c1443bdb11920f96ae78d7e627f72c535f7))
* Correct path after broken refactor ([`96f9e89`](https://github.com/JonasMuehlmann/pyaoi/commit/96f9e897f9fcfde7732dc4ed0a844de881532311))

## v0.1.0 (2020-12-26)
### Feature
* Implement search() and search_n() ([`e3a3fdb`](https://github.com/JonasMuehlmann/pyaoi/commit/e3a3fdbc1bb2d75bad704d78fcbf51843d88b339))

### Fix
* Correct config section so python-semantic-release can find it ([`8c53492`](https://github.com/JonasMuehlmann/pyaoi/commit/8c53492af651f5507201a540bda080edcabdc736))
* Correct file path ([`c70823a`](https://github.com/JonasMuehlmann/pyaoi/commit/c70823a220642cff4c87c135c18bf5e2bde80908))
* Correct bad merge after refactor and implementation change ([`d283df4`](https://github.com/JonasMuehlmann/pyaoi/commit/d283df47393af02171ca8947d2dea6f59ab5d5ba))
* Corrected syntax ([`3fb37c1`](https://github.com/JonasMuehlmann/pyaoi/commit/3fb37c1443bdb11920f96ae78d7e627f72c535f7))
* Correct path after broken refactor ([`96f9e89`](https://github.com/JonasMuehlmann/pyaoi/commit/96f9e897f9fcfde7732dc4ed0a844de881532311))
