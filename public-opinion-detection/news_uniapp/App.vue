<script>
export default {
	onLaunch: function() {
		console.log('App Launch');
	},
	onShow: function() {
		console.log('App Show');
	},
	onHide: function() {
		console.log('App Hide');
	}
};
</script>

<style>
	 @import './common/uni.css';
	 @import "./static/iconfont/iconfont.css";
	 @import './common/app.scss';
	 page{
		 position: relative;
		 background-color: #FFFFFF;
	 }
/* 解决头条小程序组件内引入字体不生效的问题 */
/* #ifdef MP-TOUTIAO */
@font-face {
	font-family: uniicons;
	src: url('/static/uni.ttf');
}
/* #endif */


</style>
