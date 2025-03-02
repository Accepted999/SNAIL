from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config

access_key = 'EVt3n4lFt5AoS1z-m2PPsPXWi-T9DnroF-fUFoyx'
secret_key = 'Q1GFWUSZ_pE4oJLqYXofj7ip4wpr3x5EthF8aQAK'


def storage(file_data):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'snail-ly-image'

    # 生成上传Token，指定过期时间
    token = q.upload_token(bucket_name, None, 3600)
    ret, info = put_data(token, None, file_data)

    if info.status_code == 200:
        # 上传成功返回文件名
        return ret.get("key")
    else:
        # 上传失败
        raise Exception("上传七牛失败")
