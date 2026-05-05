# Changelog

## 3.2.0 (2026-05-05)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/droidrun/mobilerun-sdk-python/compare/v3.1.0...v3.2.0)

### Features

* **api:** api update ([75bbc88](https://github.com/droidrun/mobilerun-sdk-python/commit/75bbc88550c6f53e16c25c692ea0febc2ed07acd))
* **api:** labels for objects ([0b8ee8c](https://github.com/droidrun/mobilerun-sdk-python/commit/0b8ee8c2cd690761a249fb97ac22c393a574f8f3))
* **api:** manual updates ([7861088](https://github.com/droidrun/mobilerun-sdk-python/commit/786108846d965ae14d619615b1d991d0cf937cb1))
* **api:** manual updates ([4579552](https://github.com/droidrun/mobilerun-sdk-python/commit/4579552f608c8de6aeab1731f512509ff049b6a4))
* support setting headers via env ([273abbc](https://github.com/droidrun/mobilerun-sdk-python/commit/273abbc5339e39f57f59d885a9bfdf5df5d2e4fe))


### Bug Fixes

* use correct field name format for multipart file arrays ([7ad94ce](https://github.com/droidrun/mobilerun-sdk-python/commit/7ad94ce83e73be25a9dc55c91aabe36065594480))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([b6562d3](https://github.com/droidrun/mobilerun-sdk-python/commit/b6562d3c3c02a73d9e7e36f26bfd6d86728993d2))


### Chores

* **internal:** more robust bootstrap script ([d8ed809](https://github.com/droidrun/mobilerun-sdk-python/commit/d8ed809f6aec7556e96cd697a8b517120cd4ebff))
* **internal:** reformat pyproject.toml ([d108c45](https://github.com/droidrun/mobilerun-sdk-python/commit/d108c45430e484b935c7ee5bd17138c2bc998d0f))

## 3.1.0 (2026-04-16)

Full Changelog: [v3.0.0...v3.1.0](https://github.com/droidrun/mobilerun-sdk-python/compare/v3.0.0...v3.1.0)

### Features

* **api:** add esim + update name endpoints ([ef39f25](https://github.com/droidrun/mobilerun-sdk-python/commit/ef39f25408689c67357e7f83d7b45e4708bb726f))
* **api:** api update ([611ce59](https://github.com/droidrun/mobilerun-sdk-python/commit/611ce5947d512e5a977e7993f420593ec584def6))
* **api:** api update ([ed0c1ff](https://github.com/droidrun/mobilerun-sdk-python/commit/ed0c1ff3d6dfae7b6d58e9558e76b3e834304218))
* **api:** api update ([4414455](https://github.com/droidrun/mobilerun-sdk-python/commit/4414455ada27ceef5219783f3a5c359fc01d045e))
* **api:** api update ([a200c8e](https://github.com/droidrun/mobilerun-sdk-python/commit/a200c8e7f2d0f27e91ca50a20dd572f81af1aeba))
* **api:** api update ([bd96644](https://github.com/droidrun/mobilerun-sdk-python/commit/bd9664417db04abc4117f56d5fa1bb8fcf502c71))
* **api:** api update ([ddd4628](https://github.com/droidrun/mobilerun-sdk-python/commit/ddd4628e1a0387e7c7f129bb0f3b3c9e48af743e))
* **api:** api update ([ca1ff6e](https://github.com/droidrun/mobilerun-sdk-python/commit/ca1ff6e9663eb72fd642cf64d131e7ca79f03c7f))
* **api:** api update ([33e9171](https://github.com/droidrun/mobilerun-sdk-python/commit/33e91716cd6d16798e3cd2d21b0c5a41cdc16260))
* **api:** api update ([5a3495e](https://github.com/droidrun/mobilerun-sdk-python/commit/5a3495e3dffb8d5d8251ae5ff32c529a82dfb6da))
* **api:** api update ([6eb34d8](https://github.com/droidrun/mobilerun-sdk-python/commit/6eb34d80a85d1bb428a2e143d879cfb40c9dcc67))
* **api:** api update ([8950157](https://github.com/droidrun/mobilerun-sdk-python/commit/8950157a39d357a5f4ba52454f558c67fb7f5a6f))
* **api:** rename mobilerun_sdk on python package ([49b126a](https://github.com/droidrun/mobilerun-sdk-python/commit/49b126ab105b5658d7cfc1cc92146ad481a94401))
* **internal:** implement indices array format for query and form serialization ([9804af6](https://github.com/droidrun/mobilerun-sdk-python/commit/9804af62e22fc18cab3c09a558255f0c537ff8e7))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([5d7ff01](https://github.com/droidrun/mobilerun-sdk-python/commit/5d7ff0187f514fb0e354202f548db24ae19a9894))
* **deps:** bump minimum typing-extensions version ([e5ee758](https://github.com/droidrun/mobilerun-sdk-python/commit/e5ee7584ab8e87a070dc8a33d27b41278a1d046a))
* ensure file data are only sent as 1 parameter ([3dfa838](https://github.com/droidrun/mobilerun-sdk-python/commit/3dfa838374a3b2948b7ec20f0457b257af9b69cb))
* **pydantic:** do not pass `by_alias` unless set ([8ef6593](https://github.com/droidrun/mobilerun-sdk-python/commit/8ef6593e4873afe4ac6d3504aa9f53b9f6cf3b2b))
* sanitize endpoint path params ([eb0325a](https://github.com/droidrun/mobilerun-sdk-python/commit/eb0325aa2bd878f09c4511502fb0270ade01ac05))


### Chores

* **ci:** skip lint on metadata-only changes ([00b1f5f](https://github.com/droidrun/mobilerun-sdk-python/commit/00b1f5f1a8fa66ff01b094d3f53edbc3b7cce8d0))
* configure new SDK language ([140b7f4](https://github.com/droidrun/mobilerun-sdk-python/commit/140b7f44d948b0b7471fcdd7e8a7c4419f06b4f0))
* **internal:** tweak CI branches ([094cdf3](https://github.com/droidrun/mobilerun-sdk-python/commit/094cdf30b65e93bc28bb7b3167d391b2b3524193))
* **internal:** update gitignore ([ac2923c](https://github.com/droidrun/mobilerun-sdk-python/commit/ac2923c6ae1b304b644f1a4f2638442b297f7dec))

## 3.0.0 (2026-03-15)

Full Changelog: [v2.1.0...v3.0.0](https://github.com/droidrun/mobilerun-sdk-python/compare/v2.1.0...v3.0.0)

### Features

* **api:** add missing endpoints ([f626748](https://github.com/droidrun/mobilerun-sdk-python/commit/f6267489f64aec8f09ae41d6858366440acb177c))
* **api:** align names with device sdk ([eac66f6](https://github.com/droidrun/mobilerun-sdk-python/commit/eac66f6ef66c3cd2d031282ad253ae5e364cfdd0))
* **api:** api update ([1250506](https://github.com/droidrun/mobilerun-sdk-python/commit/1250506c72caa3c87ea45154eafa1daf7ac3a456))
* **api:** api update ([349bc52](https://github.com/droidrun/mobilerun-sdk-python/commit/349bc52c712c3bdde72517c37b3439d09c0512f9))
* **api:** api update ([37b42e5](https://github.com/droidrun/mobilerun-sdk-python/commit/37b42e56b084278803f4ec03229a2c44d1e92c52))
* **api:** api update ([067ec92](https://github.com/droidrun/mobilerun-sdk-python/commit/067ec9243178049642f47de2772455152d677b39))
* **api:** api update ([e404031](https://github.com/droidrun/mobilerun-sdk-python/commit/e404031a09ee8dfee4608a2fa3e47a3930866dea))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([2b5a466](https://github.com/droidrun/mobilerun-sdk-python/commit/2b5a466f9ab7de499eecf1b101498dd71d3e6478))
* **internal:** add request options to SSE classes ([292b42d](https://github.com/droidrun/mobilerun-sdk-python/commit/292b42d2ad5c84a0470749dc5715ca360d36d59a))
* **internal:** codegen related update ([dfa6be3](https://github.com/droidrun/mobilerun-sdk-python/commit/dfa6be38a9014e0283c7fe1a978feae105b27d49))
* **internal:** make `test_proxy_environment_variables` more resilient ([8507955](https://github.com/droidrun/mobilerun-sdk-python/commit/8507955fdd11ce358416ada4bf7ccd65c7054ec4))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([de554a0](https://github.com/droidrun/mobilerun-sdk-python/commit/de554a039546d6363369dad00a79acf4c9431a47))
* **internal:** remove mock server code ([66af1f3](https://github.com/droidrun/mobilerun-sdk-python/commit/66af1f3e2c961b17547e79918c56c96647481567))
* update mock server docs ([213ffea](https://github.com/droidrun/mobilerun-sdk-python/commit/213ffea6a38718a522a02c8fadc4dca9efd4af03))

## 2.1.0 (2026-02-19)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/droidrun/mobilerun-sdk-python/compare/v2.0.0...v2.1.0)

### Features

* **api:** add models endpoint ([d70d5f9](https://github.com/droidrun/mobilerun-sdk-python/commit/d70d5f95155ff76900a2f90893b23bec7617a118))
* **api:** api update ([2c4273f](https://github.com/droidrun/mobilerun-sdk-python/commit/2c4273fb1fafcd2146f1a10e709ad05cfa8f2cd0))
* **api:** api update ([8800082](https://github.com/droidrun/mobilerun-sdk-python/commit/8800082d33611ed574989bc74372f7d189c32aaa))
* **api:** api update ([fdc6d3c](https://github.com/droidrun/mobilerun-sdk-python/commit/fdc6d3cd2d2ecfce66ae84ef34f8111f47fbf609))
* **api:** api update ([543bbd8](https://github.com/droidrun/mobilerun-sdk-python/commit/543bbd877819b2dc23ecfe5b3d4722996b54e92b))
* **api:** api update ([9049554](https://github.com/droidrun/mobilerun-sdk-python/commit/9049554b1ab39ca164a3351861ec41c9ea78d489))
* **api:** api update ([4c2d97d](https://github.com/droidrun/mobilerun-sdk-python/commit/4c2d97de0a1ae482871912fe677ed64e0919825e))
* **api:** api update ([8d53e63](https://github.com/droidrun/mobilerun-sdk-python/commit/8d53e63fd8ccebbe5a77af740cd5e6bdf85c2a85))
* **api:** api update ([678264c](https://github.com/droidrun/mobilerun-sdk-python/commit/678264c95364ad4fff7c70b61bd4794819f28292))
* **api:** api update ([e42aa53](https://github.com/droidrun/mobilerun-sdk-python/commit/e42aa5309759f931ceab3eee40792e559f21d3a3))
* **api:** api update ([866c20e](https://github.com/droidrun/mobilerun-sdk-python/commit/866c20ec6ebd177c861777fee900259186347ef0))
* **api:** api update ([416142e](https://github.com/droidrun/mobilerun-sdk-python/commit/416142eb345a07aefea8404a97231ed0acd74678))
* **api:** expose device count endpoint ([ab1191d](https://github.com/droidrun/mobilerun-sdk-python/commit/ab1191d28943441844e81c6c1189aebc34f54980))
* **api:** manual updates ([bf2a897](https://github.com/droidrun/mobilerun-sdk-python/commit/bf2a897dce0c3771858892a9497acdf9dcddeb93))
* **api:** manual updates ([e529cf6](https://github.com/droidrun/mobilerun-sdk-python/commit/e529cf666a09be899a1af449735a2759b307762b))
* **api:** manual updates ([a27d844](https://github.com/droidrun/mobilerun-sdk-python/commit/a27d844d5ca5cecc754a2a3e0eb88712a8540d43))
* **client:** add custom JSON encoder for extended type support ([9471952](https://github.com/droidrun/mobilerun-sdk-python/commit/947195285cae03d555b21716015384cc2e1f3fa0))
* **client:** add support for binary request streaming ([c6668af](https://github.com/droidrun/mobilerun-sdk-python/commit/c6668af5dbd83d7ab1dd1fe4f68253422e055e73))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([a06f4b2](https://github.com/droidrun/mobilerun-sdk-python/commit/a06f4b2146dafd2c9435fecb603a6217b085fcc5))


### Chores

* **ci:** upgrade `actions/github-script` ([00033ad](https://github.com/droidrun/mobilerun-sdk-python/commit/00033ad7ffac1d3d650a05e841bbdecca964192e))
* format all `api.md` files ([2910e43](https://github.com/droidrun/mobilerun-sdk-python/commit/2910e4312fa6360f754de4d6937d677cd04acc68))
* **internal:** bump dependencies ([91ab063](https://github.com/droidrun/mobilerun-sdk-python/commit/91ab0631121c4ca096133953344ea83e96cc32ae))
* **internal:** fix lint error on Python 3.14 ([f5920bc](https://github.com/droidrun/mobilerun-sdk-python/commit/f5920bc46fb52360860c02ca941926e939f3e316))
* **internal:** update `actions/checkout` version ([75af377](https://github.com/droidrun/mobilerun-sdk-python/commit/75af377b29fca57b52843186af3e9775bfc78c13))

## 2.0.0 (2026-01-12)

Full Changelog: [v0.1.0...v2.0.0](https://github.com/droidrun/mobilerun-sdk-python/compare/v0.1.0...v2.0.0)

### Features

* **api:** add devices.tasks.list ([797024f](https://github.com/droidrun/mobilerun-sdk-python/commit/797024fbae9d474897ecb70a368e0615b683d8e8))
* **api:** api update ([5eb4b01](https://github.com/droidrun/mobilerun-sdk-python/commit/5eb4b0159d48560cda44789cb6225dd42c543314))
* **api:** api update ([b816d3d](https://github.com/droidrun/mobilerun-sdk-python/commit/b816d3d9547b2f2544d4609d27ddc67a789fa968))
* **api:** api update ([3362213](https://github.com/droidrun/mobilerun-sdk-python/commit/3362213819e07ec63854f7f6dc1caaed5f2424ba))
* **api:** api update ([173b208](https://github.com/droidrun/mobilerun-sdk-python/commit/173b208d9d76f5392423276f663dff6a97ac67de))
* **api:** api update ([4d02912](https://github.com/droidrun/mobilerun-sdk-python/commit/4d029123152d3901ddfab5024bb99bcc0a606ed0))
* **api:** api update ([0c20a35](https://github.com/droidrun/mobilerun-sdk-python/commit/0c20a35249ffa0f4ae48c9cded6e4ea1fa377a71))
* **api:** api update ([ca58e17](https://github.com/droidrun/mobilerun-sdk-python/commit/ca58e17885d6d9ba48a869445b974b0e7158e877))
* **api:** api update ([de292ad](https://github.com/droidrun/mobilerun-sdk-python/commit/de292ad6e5c7809c4902d6aee59c8d23c9ab2da8))
* **api:** api update ([d101779](https://github.com/droidrun/mobilerun-sdk-python/commit/d101779d3dfc333b1f0cafc85c6ab663dd407a55))
* **api:** api update ([63686e1](https://github.com/droidrun/mobilerun-sdk-python/commit/63686e1f4aab1fd67d61d62b51969b757d4b3011))
* **api:** api update ([82f0b5d](https://github.com/droidrun/mobilerun-sdk-python/commit/82f0b5dad385fc5da9fafa5940eed7c483f83d38))
* **api:** api update ([4f46d03](https://github.com/droidrun/mobilerun-sdk-python/commit/4f46d0391dcdb93d2468021ab20628ab669e97dc))
* **api:** api update ([8a1adbe](https://github.com/droidrun/mobilerun-sdk-python/commit/8a1adbed5f6aeb665545717c907085c40c4f008d))
* **api:** api update ([29e7952](https://github.com/droidrun/mobilerun-sdk-python/commit/29e79521aa0057d0f3b929f9c963348ec0b4125a))
* **api:** api update ([280aa69](https://github.com/droidrun/mobilerun-sdk-python/commit/280aa699acae6a368ad7ab1d7e04a15b4b8bb97b))
* **api:** api update ([6473505](https://github.com/droidrun/mobilerun-sdk-python/commit/64735056155d700df59aca2f17e366778e83bd44))


### Bug Fixes

* **client:** loosen auth header validation ([2f47451](https://github.com/droidrun/mobilerun-sdk-python/commit/2f474519c1b196c69acda9f5b4bf256847cdccdf))
* **models:** add element node stainless config ([64a27e6](https://github.com/droidrun/mobilerun-sdk-python/commit/64a27e6a852ec43c757e6d1d7b3cff6367f7ee28))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([c521873](https://github.com/droidrun/mobilerun-sdk-python/commit/c521873828d181c3e5a9761742ca70c1185dc28c))

## 0.1.0 (2025-12-23)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/droidrun/mobilerun-sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** add devices.actions.global ([3ce14b3](https://github.com/droidrun/mobilerun-sdk-python/commit/3ce14b3d3654739f8d5d06d115b6813879f1de30))
* **api:** added endpoints for hooks and ui_states retrieval ([eb57807](https://github.com/droidrun/mobilerun-sdk-python/commit/eb578079583da65155fed36828dce1df2ac0459f))
* **api:** api update ([25063e2](https://github.com/droidrun/mobilerun-sdk-python/commit/25063e2c6effa8f6e700b9cca00829c34c06df8f))
* **api:** api update ([3e0a589](https://github.com/droidrun/mobilerun-sdk-python/commit/3e0a589e1f5b143b82ff7d7ca5e7ea5ad416a2fa))
* **api:** api update ([d46fbfb](https://github.com/droidrun/mobilerun-sdk-python/commit/d46fbfb491a92a32c047f043a35360d4511e1ac8))
* **api:** api update ([3a514fe](https://github.com/droidrun/mobilerun-sdk-python/commit/3a514fe21029fa65354b3d471b20cf4c25543bbd))
* **api:** api update ([8ead677](https://github.com/droidrun/mobilerun-sdk-python/commit/8ead677c34ada10a769ba29412c9e83aaf29e447))
* **api:** api update ([fcd3922](https://github.com/droidrun/mobilerun-sdk-python/commit/fcd39224e4d628208a359223db4863eb78be0a85))
* **api:** api update ([2cbc333](https://github.com/droidrun/mobilerun-sdk-python/commit/2cbc333f662be2f49bca4003563674e4019fd0d7))
* **api:** api update ([60db72a](https://github.com/droidrun/mobilerun-sdk-python/commit/60db72ac37e76963dafa9c478933edb298e34f4f))
* **api:** api update ([b4a5392](https://github.com/droidrun/mobilerun-sdk-python/commit/b4a539276412316465e883d4dd89453c66d2f82b))
* **api:** api update ([1d65e40](https://github.com/droidrun/mobilerun-sdk-python/commit/1d65e403cb0070d7c30fb9498cc6af25bbe12b22))
* **api:** api update ([9c968bd](https://github.com/droidrun/mobilerun-sdk-python/commit/9c968bdbc1a5bd410a07433beac653dcd5980068))
* **api:** api update ([dd8393b](https://github.com/droidrun/mobilerun-sdk-python/commit/dd8393bcfd71701542dd3f2a2777dc391a6fa84b))
* **api:** api update ([8c59a75](https://github.com/droidrun/mobilerun-sdk-python/commit/8c59a75d2e580a15c576c297a8ccf2fa4238ea75))
* **api:** api update ([0365eb9](https://github.com/droidrun/mobilerun-sdk-python/commit/0365eb930ce8930c9022db4e27b1422b10f41ffb))
* **api:** api update ([d09ba89](https://github.com/droidrun/mobilerun-sdk-python/commit/d09ba89ab97834d00bc4521ef6b897b8bf558994))
* **api:** api update ([7e21eb4](https://github.com/droidrun/mobilerun-sdk-python/commit/7e21eb4468ee6ffbef4e680091488ee5d9f0a0d5))
* **api:** api update ([8e387ef](https://github.com/droidrun/mobilerun-sdk-python/commit/8e387ef6b2e76a8528639c2b111ba29f509fbb19))
* **api:** api update ([00e7bb8](https://github.com/droidrun/mobilerun-sdk-python/commit/00e7bb8df4c1ac37da2c0e02905c3b9d28f0d866))
* **api:** api update ([dd3f1b4](https://github.com/droidrun/mobilerun-sdk-python/commit/dd3f1b4f80c8b737a1831c8916d66a7e04a1d95c))
* **api:** api update ([c5b3ad5](https://github.com/droidrun/mobilerun-sdk-python/commit/c5b3ad5d9ae7f186737c57dcb9d30f5a25fd01ea))
* **api:** api update ([3ae8d53](https://github.com/droidrun/mobilerun-sdk-python/commit/3ae8d53836b675515e31686f30d2758a9f3d4e78))
* **api:** api update ([0cd3588](https://github.com/droidrun/mobilerun-sdk-python/commit/0cd35884d5bb0a0ae6092f210e9908e0a45d9c2c))
* **api:** api update ([86932c0](https://github.com/droidrun/mobilerun-sdk-python/commit/86932c00c63ffc1ae84f11f20864fc9d3a76d500))
* **api:** api update ([bfc81eb](https://github.com/droidrun/mobilerun-sdk-python/commit/bfc81eb028fb2225c46d6c9862f5ec6f9bffb8e2))
* **api:** api update ([5418c21](https://github.com/droidrun/mobilerun-sdk-python/commit/5418c211ec1d83cf8855760e40681d74fb975a17))
* **api:** api update ([89b79f1](https://github.com/droidrun/mobilerun-sdk-python/commit/89b79f14a75143499b54d084ef5faebf9792f96d))
* **api:** api update ([c2e4beb](https://github.com/droidrun/mobilerun-sdk-python/commit/c2e4beb5b3d4bf215b9780428277ee6391e508f3))
* **api:** api update ([4e24371](https://github.com/droidrun/mobilerun-sdk-python/commit/4e2437134f7912690347a32f60cfb7d1bce83106))
* **api:** api update ([4d0dd72](https://github.com/droidrun/mobilerun-sdk-python/commit/4d0dd7217655e59ef7fcdc41b77e5b99442add2b))
* **api:** api update ([a4bd71f](https://github.com/droidrun/mobilerun-sdk-python/commit/a4bd71fc2266d655321d3a8db182d5edc7fcddd3))
* **api:** api update ([1f550af](https://github.com/droidrun/mobilerun-sdk-python/commit/1f550af3d3ff24d9069d39bff1e2d9dcb8b755a7))
* **api:** api update ([1e14222](https://github.com/droidrun/mobilerun-sdk-python/commit/1e14222c957a47e30c8f60a8f45f8e6c2cb741de))
* **api:** api update ([f182b6f](https://github.com/droidrun/mobilerun-sdk-python/commit/f182b6f6747c1cb877c251d25fad7722f167d22c))
* **api:** cleanup ([5122220](https://github.com/droidrun/mobilerun-sdk-python/commit/5122220431e75d4f15cff30775c7d5fa06a123ac))
* **api:** devices methods ([d230b5e](https://github.com/droidrun/mobilerun-sdk-python/commit/d230b5e325a0c7ebcf8819fb848a61ac19d6d433))
* **api:** make key optional ([178d3e0](https://github.com/droidrun/mobilerun-sdk-python/commit/178d3e0ffe660b88260af2b82080836876b7b080))
* **api:** remove testing environments ([d512e7c](https://github.com/droidrun/mobilerun-sdk-python/commit/d512e7c04e9091813fea58a74beec262e19df6bc))
* **api:** update docs url ([9855c10](https://github.com/droidrun/mobilerun-sdk-python/commit/9855c1006e2d62241f58a3459ee691183d874bfc))
* **api:** update organisation name to mobilerun ([df021e8](https://github.com/droidrun/mobilerun-sdk-python/commit/df021e81a38607fb9f15d0edd8e3197035ed0410))
* **api:** update to mobilerun ([b895845](https://github.com/droidrun/mobilerun-sdk-python/commit/b895845db34fe00ad2798d1b3f38649e227ec128))


### Bug Fixes

* **api:** rename python package to mobilerun-sdk ([ad149d2](https://github.com/droidrun/mobilerun-sdk-python/commit/ad149d2f1201c301ecccef4f63ea985eb34977bd))
* compat with Python 3.14 ([4c52e9c](https://github.com/droidrun/mobilerun-sdk-python/commit/4c52e9cd81ec0d8a649cf00f7d9db2016122606c))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([8241787](https://github.com/droidrun/mobilerun-sdk-python/commit/8241787d7b1e8a49f655554ad755c573333239b2))
* ensure streams are always closed ([9f4cf2e](https://github.com/droidrun/mobilerun-sdk-python/commit/9f4cf2eddd7ce189ca4820fe55e676fd1edd35cd))
* use async_to_httpx_files in patch method ([f2b25d8](https://github.com/droidrun/mobilerun-sdk-python/commit/f2b25d8d87201bc41f6a13b722e42200ed793892))


### Chores

* add Python 3.14 classifier and testing ([3c8ae3e](https://github.com/droidrun/mobilerun-sdk-python/commit/3c8ae3ee616004428d7d1cd4e4c1da6fa60fc93b))
* configure new SDK language ([28af809](https://github.com/droidrun/mobilerun-sdk-python/commit/28af809398b7c625e99ce2f3de78e4fc8d84934c))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([62e19d3](https://github.com/droidrun/mobilerun-sdk-python/commit/62e19d3e954e2cd6cfcc803155b4c9594df8022b))
* **docs:** use environment variables for authentication in code snippets ([b67d5c9](https://github.com/droidrun/mobilerun-sdk-python/commit/b67d5c9f8d67215a9a8b60702d7a8b13902e6b01))
* **internal:** add `--fix` argument to lint script ([4040a9d](https://github.com/droidrun/mobilerun-sdk-python/commit/4040a9db869b06e26e1180990d831f8578cc16af))
* **internal:** add missing files argument to base client ([907c05f](https://github.com/droidrun/mobilerun-sdk-python/commit/907c05f68e6826508b569fa7735887ad2cbd6078))
* **internal:** codegen related update ([922238d](https://github.com/droidrun/mobilerun-sdk-python/commit/922238dc53292f30be3cb3dccc1391b2651acf29))
* **package:** drop Python 3.8 support ([7e89ce9](https://github.com/droidrun/mobilerun-sdk-python/commit/7e89ce956df58a73182140edc57102c5460dd6dd))
* speedup initial import ([9ee3621](https://github.com/droidrun/mobilerun-sdk-python/commit/9ee3621562a85b2adffb29a529bc4f1a717a7780))
* update lockfile ([18d5296](https://github.com/droidrun/mobilerun-sdk-python/commit/18d5296092553095eb5ab165e3157b761fcc2e12))
* update SDK settings ([8de53cb](https://github.com/droidrun/mobilerun-sdk-python/commit/8de53cb37f49d4e99937fd1a421881866b0a2d44))
* update SDK settings ([db9f34b](https://github.com/droidrun/mobilerun-sdk-python/commit/db9f34bc46db016e88e2c86bb81c4da062d7c35a))
