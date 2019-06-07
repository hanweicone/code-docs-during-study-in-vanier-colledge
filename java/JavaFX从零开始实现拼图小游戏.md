<main>

<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# 【java】JavaFX从零开始实现拼图小游戏

</div>

<div class="article-info-box">

<div class="article-bar-top"><span class="time">2018年12月05日 21:14:39</span> [以后我要当村长](https://me.csdn.net/qq_42370146) <span class="read-count">阅读数：582</span></div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post"><link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css"> <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">

<div class="htmledit_views" id="content_views">

**最近java课老师布置了一个作业：制作一个拼图小游戏，关键老师自己说javaGUI编程没用，讲课的时候好像跳过了（没去上课不过我猜应该没讲吧），现在又叫我们做这些，实在是哭笑不得。**

**得了吧，老师的任务只能老老实实完成对吧，但是我又想到像Swing这些工具包已经基本上被淘汰了，做出来的页面有点老土，要学就学点好的，于是我选择用JavaFX来完成这次作业。**

**JavaFX的发展也不容乐观，一直不温不火的，但是本着对桌面应用有着一定的兴趣，就学一学吧，于是学了半天后开始上手做出来这个极其简陋的拼图游戏，希望随之以后的深入学习，能够做出更精美的应用。**

## <a name="t0"></a>**（一）首页界面**

![](https://img-blog.csdnimg.cn/20181205200106845.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMzcwMTQ2,size_16,color_FFFFFF,t_70)

 **首页就很简单，一个VBox作为父布局，嵌套一个HBox子布局，HBox子布局里写三个Button事件，点击后打开指定难度的窗体，并关闭首页窗体，下面的文本是放在父布局VBox里的Label的文本内容，至于背景和按钮颜色则是用css来指定，整个过程唯一要关注的就是各个按钮大小间距位置等等。**

## <a name="t1"></a>**（二）游戏界面**

**在游戏中我设置了三种难度，分别是3*3，4*4，5*5，实现上基本一样，所以只讲第一个简单难度九宫格的实现即可。**

**点击简单按钮后，关闭首页窗口，打开游戏窗口：**

![](https://img-blog.csdnimg.cn/2018120520122217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMzcwMTQ2,size_16,color_FFFFFF,t_70)

**讲这个页面的难点（其实也很简单）：**

**（1）** **图片的截取：我当然不是PS去把一张图片截成一块块图片啦，这里我用imageview.setViewPort(new Rectangle2D （x,y,width,higth）)的方法进行切割，可以指定图片从哪儿开始切，以及需要的图片大小**

**（2）图片的存储：利用图片数组ImageView[ ]存储切割好的图片即可，每一个数组元素里就是完整图片的一个子图片**

**（3）图片在九宫格中的摆放：利用GridPane布局，可以指定在布局里图片的位置，达到九宫格的效果**

**（4）图片摆放后必须有解：学名叫N数码问题，看了一些大神的博客以下结论：**

**                       当列数为奇数时,一切操作不影响奇偶性,当前状态逆序数为偶数等价于拼图有解**

**                       当列数为偶数时,上下交换影响奇偶性,只要当前状态逆序数奇偶性^当前空格状态的奇偶性=偶数等价于拼图有解**

**（5）实现拼图有解：由上面的结论我们可以这样，从[0-8]中随机取8个不重复的数字，保证这串数字的逆序数为偶数，例如：[2 0 1 3 4 5 6 7]，没有获得的数字为[8],首先令索引为8图片数组存储一个空白图片，然后我们把这串数字作为图片数组i的下标，分别把图片放在对应九宫格的位置，如：**

**i[2]  i[0]  i[1]**

**i[3]  i[4]  i[5]**

**i[6]  i[7]  <span style="color:#f33b45;">i[8]----->存储空白图片</span>**

**（6）图片的移动：点击空白格子周围的格子，实现图片在布局中的位置交换即可，如点击i[7]实现交换：**

**i[2]  i[0]  i[1]**

**i[3]  i[4]  i[5]**

**i[6]  <span style="color:#f33b45;">i[8]   </span>i[7]**

**（7）如何算作拼图成功：每一次图片交换，就检查是否拼图成功，至于是否拼图成功想必可以很直观的看出来，我们是顺序切割图片再顺序存储，因此像这样就能判定成功：**

**i[0]  i[1]  i[2]    **

**i[3]  i[4]  i[5]**

**i[6]  i[7]  <span style="color:#f33b45;">i[8]   </span>**

（**8**）**判定拼图成功：我们需要判定数组下标是不是在它需要对应的位置，数学化后的公式为：n = 3 * r + c，n为数组下标，r为行的索引，c为列的索引，如i[4]下标为4，行索引为1，列索引为1，可得：4=n=1*3+1=4，显然可证该图片所处的位置是正确的**

**（9）下方按钮事件：返回首页即关闭当前窗口再打开首页窗口，重新游戏即关闭当前窗口再打开游戏窗口，显示原图相当于提示功能，在不关闭当前窗口的前提下，打开另一个显示完整图片的窗口**

## <a name="t2"></a>**（三）游戏成功界面**

![](https://img-blog.csdnimg.cn/20181205210815296.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMzcwMTQ2,size_16,color_FFFFFF,t_70)

**没什么难度，当检测拼图成功时弹出一个文本框即可。**

## <a name="t3"></a>**（四）源码部分**

**（1）首页界面**

    import javafx.application.Application;import javafx.event.ActionEvent;import javafx.event.EventHandler;import javafx.geometry.Insets;import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.control.Button;import javafx.scene.control.Label;import javafx.scene.image.Image;import javafx.scene.layout.HBox;import javafx.scene.layout.VBox;import javafx.scene.paint.Color;import javafx.scene.text.Font; /***开始菜单主界面*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class Start extends Application { 	@Override	public void start(Stage primaryStage) {		try {			// 父容器			VBox vBox = new VBox(); 			// 子容器,分别是按钮和输出文本			HBox hBox_1 = new HBox();			HBox hBox_2 = new HBox(); 			// 显示难度选择按钮			Button start_1 = new Button("简单");			start_1.setOnAction(new EventHandler<ActionEvent>() {				@Override				public void handle(ActionEvent arg0) {					// 打开另一个窗口，即游戏窗口					Game_1 game_1 = new Game_1();					game_1.start(new Stage());					// 关闭开始界面					primaryStage.close();				}			});			Button start_2 = new Button("困难");			start_2.setOnAction(new EventHandler<ActionEvent>() {				@Override				public void handle(ActionEvent arg0) {					// 打开另一个窗口，即游戏窗口					Game_2 game_2 = new Game_2();					game_2.start(new Stage());					// 关闭开始界面					primaryStage.close();				}			});			Button start_3 = new Button("地狱");			start_3.setOnAction(new EventHandler<ActionEvent>() {				@Override				public void handle(ActionEvent arg0) {					// 打开另一个窗口，即游戏窗口					Game_3 game_3 = new Game_3();					game_3.start(new Stage());					// 关闭开始界面					primaryStage.close();				}			}); 			Label label = new Label("@余氏出品，必属渣品");			//设置文本样式大小和颜色			label.setFont(new Font("Arial", 30));			label.setTextFill(Color.web("black"));						hBox_1.getChildren().addAll(start_1, start_2, start_3);			hBox_2.getChildren().add(label);			vBox.getChildren().addAll(hBox_1, hBox_2); 			// 设置按钮大小并调节位置			start_1.setPrefSize(100, 60);			start_2.setPrefSize(100, 60);			start_3.setPrefSize(100, 60);			hBox_1.setPadding(new Insets(650, 100, 0, 175));			hBox_2.setPadding(new Insets(50, 50, 500, 260));			// 设置控件之间的距离			hBox_1.setSpacing(100); 			// 标题栏图标			Image image = new Image("application/4.jpg"); 			Scene scene = new Scene(vBox, 800, 800);			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());			primaryStage.getIcons().add(image);			primaryStage.setTitle("智障拼图");			primaryStage.setScene(scene);			primaryStage.setResizable(false);			primaryStage.show();		} catch (Exception e) {			e.printStackTrace();		}	} 	public static void main(String[] args) {		launch(args);	}}

**（2）简单难度的游戏界面 **

    import java.util.Random; import javafx.application.Application;import javafx.event.ActionEvent;import javafx.event.EventHandler;import javafx.geometry.Insets;import javafx.geometry.Pos;import javafx.geometry.Rectangle2D;import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.control.Alert;import javafx.scene.control.Button;import javafx.scene.control.Alert.AlertType;import javafx.scene.image.Image;import javafx.scene.image.ImageView;import javafx.scene.input.MouseEvent;import javafx.scene.layout.GridPane;import javafx.scene.layout.HBox;import javafx.scene.layout.VBox;/***游戏界面----简单*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class Game_1 extends Application {	public int m; // m是不在随机数组的那个数字	ImageView[] imageViews = new ImageView[9]; 	@Override	public void start(Stage primaryStage) {		init(primaryStage); 	} 	public void init(Stage primaryStage) {		// 父布局		VBox vBox = new VBox(); 		// 3*3九宫格布局，作为上方的选项嵌套入父布局		GridPane gridPane = new GridPane(); 		// 水平布局，作为下方的选项嵌套入父布局		HBox hbox = new HBox();		hbox.setPadding(new Insets(10)); // 填充		hbox.setAlignment(Pos.CENTER); // 居中 		// 添加3个点击		Button home = new Button("返回首页");		home.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即首页窗口				Start start = new Start();				start.start(new Stage());				// 关闭原本界面				primaryStage.close();			}		});		Button again = new Button("重新游戏");		again.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即游戏窗口				Game_1 game = new Game_1();				game.start(new Stage());				// 关闭原本界面				primaryStage.close();			}		});		Button look = new Button("查看原图");		look.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即显示原图				OnImage_1 OnImage = new OnImage_1();				OnImage.start(new Stage());			}		});		// 设置按钮大小并居中		home.setPrefSize(200, 50);		again.setPrefSize(200, 50);		look.setPrefSize(200, 50);		// 设置控件之间的距离		hbox.setSpacing(100); 		hbox.getChildren().addAll(home,again, look); 		// 游戏部分		/*		 * 自定义的函数，产生逆序数为偶数的不重复数组,依次作为图片数组的下标，例如: 2 0 1 3 4 5 6 7 ------>，此时m=8,变成如下即为正确：		 * 0 1 2 3 4 5 4 7		 */		int[] n = random(); 		Image image2 = new Image("application/2.jpg"); 		for (int i = 0; i < 9; i++) {			imageViews[i] = new ImageView(image2); // 初始化数组			imageViews[i].setOnMouseClicked(new myevent()); // 设置点击事件		}		for (int i = 0, k = 0; i <= 2; i++) {			for (int j = 0; j <= 2; j++, k++) {				imageViews[k].setViewport(new Rectangle2D(250 * j, 250 * i, 250, 250)); // 切割图片分配给图片数组			}		}		// 按照产生的随机数将imageView数组加入面板		gridPane.add(imageViews[n[0]], 0, 0);		gridPane.add(imageViews[n[1]], 1, 0);		gridPane.add(imageViews[n[2]], 2, 0);		gridPane.add(imageViews[n[3]], 0, 1);		gridPane.add(imageViews[n[4]], 1, 1);		gridPane.add(imageViews[n[5]], 2, 1);		gridPane.add(imageViews[n[6]], 0, 2);		gridPane.add(imageViews[n[7]], 1, 2);		m = findnum(n); // 找出那个不在随机数组里面的数字 		Image image1 = new Image("application/3.jpg"); // 3.png为一个透明图，放在空格子中		imageViews[m].setImage(image1);		gridPane.add(imageViews[m], 2, 2);		gridPane.setGridLinesVisible(true);		gridPane.setPrefWidth(800);		gridPane.setPrefHeight(700);		vBox.getChildren().add(gridPane);		// 布局嵌套，选项部分		vBox.getChildren().add(hbox); 		// 标题栏图标		Image image = new Image("application/4.jpg"); 		Scene scene = new Scene(vBox, 800, 800);		scene.getStylesheets().add(getClass().getResource("Game.css").toExternalForm());		primaryStage.getIcons().add(image);		primaryStage.setTitle("智障拼图");		primaryStage.setScene(scene);		primaryStage.setResizable(false);		primaryStage.show();	} 	public int[] random() { // 生成8个不重复的逆序数为偶数的数字,这样拼图才有结		int[] ran = new int[8];		while (iso(ran) == false) {			ran = random_num();		}		return ran; 	} 	public int[] random_num() { // 生成8个不重复数		int r[] = new int[8];		Random random = new Random();		for (int i = 0; i < 8; ++i) {			r[i] = random.nextInt(9);			for (int j = 0; j < i; ++j) {				while (r[i] == r[j]) {					i--;					break;				}			}		}		return r;	} 	// 判断逆序数是否为偶数	public boolean iso(int[] num) {		int sum = 0;		for (int i = 0; i <= 6; ++i) {			for (int j = i; j <= 7; j++) {				if (num[i] > num[j]) {					sum++;				}			}		}		if ((sum % 2) == 0 && sum != 0) {			return true;		} 		return false; 	} 	// 点击事件的实现	class myevent implements EventHandler<MouseEvent> { 		@Override		public void handle(MouseEvent arg0) { 			ImageView img = (ImageView) arg0.getSource();			double sx = img.getLayoutX();			double sy = img.getLayoutY();			double dispx = sx - imageViews[m].getLayoutX();			double dispy = sy - imageViews[m].getLayoutY();			if ((dispx == -250) && (dispy == 0)) { // 点击的空格左边的格子				swapimg(img, imageViews[m]); // 交换imageView				if (issucc(imageViews)) { // 判断是否拼成功					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} 			else if ((dispx == 0) && (dispy == -250)) { // 上面的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} else if ((dispx == 250) && (dispy == 0)) { // 右边的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} else if ((dispx == 0) && (dispy == 250)) { // 下面的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			}		} 		// 交换两个imageView的实现		public void swapimg(ImageView i1, ImageView i2) {			int row1 = GridPane.getRowIndex(i1);			int colu1 = GridPane.getColumnIndex(i1);			int row2 = GridPane.getRowIndex(i2);			int colu2 = GridPane.getColumnIndex(i2);			GridPane.setRowIndex(i1, row2);			GridPane.setColumnIndex(i1, colu2);			GridPane.setRowIndex(i2, row1);			GridPane.setColumnIndex(i2, colu1);		}	} 	// 判断是否拼图成功	public boolean issucc(ImageView[] imageViews) {		for (int i = 0; i <= 8; ++i) {			if (i != 3 * GridPane.getRowIndex(imageViews[i]) + GridPane.getColumnIndex(imageViews[i])) {				return false;			}		}		return true;	} 	// 找出m	public int findnum(int[] n) {		for (int j = 0; j <= 8; ++j) {			if ((j == n[0]) || (j == n[1]) || (j == n[2]) || (j == n[3]) || (j == n[4]) || (j == n[5]) || (j == n[6])					|| (j == n[7])) {			} else {				return j;			}		}		return -1;	} }

**（3）困难难度的游戏界面 **

    import java.util.Random; import javafx.application.Application;import javafx.event.ActionEvent;import javafx.event.EventHandler;import javafx.geometry.Insets;import javafx.geometry.Pos;import javafx.geometry.Rectangle2D;import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.control.Alert;import javafx.scene.control.Button;import javafx.scene.control.Alert.AlertType;import javafx.scene.image.Image;import javafx.scene.image.ImageView;import javafx.scene.input.MouseEvent;import javafx.scene.layout.GridPane;import javafx.scene.layout.HBox;import javafx.scene.layout.VBox;/***游戏界面----困难*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class Game_2 extends Application {	public int m; // m是不在随机数组的那个数字	ImageView[] imageViews = new ImageView[16]; 	@Override	public void start(Stage primaryStage) {		init(primaryStage); 	} 	public void init(Stage primaryStage) {		// 父布局		VBox vBox = new VBox(); 		// 3*3九宫格布局，作为上方的选项嵌套入父布局		GridPane gridPane = new GridPane(); 		// 水平布局，作为下方的选项嵌套入父布局		HBox hbox = new HBox();		hbox.setPadding(new Insets(10)); // 填充		hbox.setAlignment(Pos.CENTER); // 居中 		// 添加3个点击		Button home = new Button("返回首页");		home.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即首页窗口				Start start = new Start();				start.start(new Stage());				// 关闭原本界面				primaryStage.close();			}		});		Button again = new Button("重新游戏");		again.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即游戏窗口				Game_2 game = new Game_2();				game.start(new Stage());				// 关闭开始界面				primaryStage.close();			}		});		Button look = new Button("查看原图");		look.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即显示原图				OnImage_2 OnImage = new OnImage_2();				OnImage.start(new Stage());			}		});		// 设置按钮大小并居中		home.setPrefSize(200, 50);		again.setPrefSize(200, 50);		look.setPrefSize(200, 50);		// 设置控件之间的距离		hbox.setSpacing(100); 		hbox.getChildren().addAll(home,again, look); 		// 游戏部分		/*		 * 自定义的函数，产生逆序数为偶数的不重复数组,依次作为图片数组的下标，例如: 2 0 1 3 4 5 6 7 ------>，此时m=8,变成如下即为正确：		 * 0 1 2 3 4 5 4 7		 */		int[] n = random(); 		Image image2 = new Image("application/2_1.jpg"); 		for (int i = 0; i < 16; i++) {			imageViews[i] = new ImageView(image2); // 初始化数组			imageViews[i].setOnMouseClicked(new myevent()); // 设置点击事件		}		for (int i = 0, k = 0; i <= 3; i++) {			for (int j = 0; j <= 3; j++, k++) {				imageViews[k].setViewport(new Rectangle2D(150 * j, 150 * i, 150, 150)); // 切割图片分配给图片数组			}		}		// 按照产生的随机数将imageView数组加入面板		gridPane.add(imageViews[n[0]], 0, 0);		gridPane.add(imageViews[n[1]], 1, 0);		gridPane.add(imageViews[n[2]], 2, 0);		gridPane.add(imageViews[n[3]], 3, 0);		gridPane.add(imageViews[n[4]], 0, 1);		gridPane.add(imageViews[n[5]], 1, 1);		gridPane.add(imageViews[n[6]], 2, 1);		gridPane.add(imageViews[n[7]], 3, 1);		gridPane.add(imageViews[n[8]], 0, 2);		gridPane.add(imageViews[n[9]], 1, 2);		gridPane.add(imageViews[n[10]], 2, 2);		gridPane.add(imageViews[n[11]], 3, 2);		gridPane.add(imageViews[n[12]], 0, 3);		gridPane.add(imageViews[n[13]], 1, 3);		gridPane.add(imageViews[n[14]], 2, 3);		m = findnum(n); // 找出那个不在随机数组里面的数字 		Image image1 = new Image("application/3.jpg"); // 3.png为一个透明图，放在空格子中		imageViews[m].setImage(image1);		gridPane.add(imageViews[m], 3, 3);		gridPane.setGridLinesVisible(true);		gridPane.setPrefWidth(800);		gridPane.setPrefHeight(700);		vBox.getChildren().add(gridPane);		// 布局嵌套，选项部分		vBox.getChildren().add(hbox); 		// 标题栏图标		Image image = new Image("application/4.jpg"); 		Scene scene = new Scene(vBox, 800, 800);		scene.getStylesheets().add(getClass().getResource("Game.css").toExternalForm());		primaryStage.getIcons().add(image);		primaryStage.setTitle("智障拼图");		primaryStage.setScene(scene);		primaryStage.setResizable(false);		primaryStage.show();	} 	public int[] random() { // 生成15个不重复的逆序数为偶数的数字,这样拼图才有结		int[] ran = new int[15];		while (iso(ran) == false) {			ran = random_num();		}		return ran; 	} 	public int[] random_num() { // 生成15个不重复数		int r[] = new int[15];		Random random = new Random();		for (int i = 0; i < 15; ++i) {			r[i] = random.nextInt(16);			for (int j = 0; j < i; ++j) {				while (r[i] == r[j]) {					i--;					break;				}			}		}		return r;	} 	// 判断逆序数是否为偶数	public boolean iso(int[] num) {		int sum = 0;		for (int i = 0; i <= 13; ++i) {			for (int j = i; j <= 14; j++) {				if (num[i] > num[j]) {					sum++;				}			}		}		if ((sum % 2) == 0 && sum != 0) {			return true;		} 		return false; 	} 	// 点击事件的实现	class myevent implements EventHandler<MouseEvent> { 		@Override		public void handle(MouseEvent arg0) { 			ImageView img = (ImageView) arg0.getSource();			double sx = img.getLayoutX();			double sy = img.getLayoutY();			double dispx = sx - imageViews[m].getLayoutX();			double dispy = sy - imageViews[m].getLayoutY();			if ((dispx == -150) && (dispy == 0)) { // 点击的空格左边的格子				swapimg(img, imageViews[m]); // 交换imageView				if (issucc(imageViews)) { // 判断是否拼成功					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} 			else if ((dispx == 0) && (dispy == -150)) { // 上面的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} else if ((dispx == 150) && (dispy == 0)) { // 右边的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} else if ((dispx == 0) && (dispy == 150)) { // 下面的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			}		} 		// 交换两个imageView的实现		public void swapimg(ImageView i1, ImageView i2) {			int row1 = GridPane.getRowIndex(i1);			int colu1 = GridPane.getColumnIndex(i1);			int row2 = GridPane.getRowIndex(i2);			int colu2 = GridPane.getColumnIndex(i2);			GridPane.setRowIndex(i1, row2);			GridPane.setColumnIndex(i1, colu2);			GridPane.setRowIndex(i2, row1);			GridPane.setColumnIndex(i2, colu1);		}	} 	// 判断是否拼图成功	public boolean issucc(ImageView[] imageViews) {		for (int i = 0; i <= 15; ++i) {			if (i != 3 * GridPane.getRowIndex(imageViews[i]) + GridPane.getColumnIndex(imageViews[i])) {				return false;			}		}		return true;	} 	// 找出m	public int findnum(int[] n) {		for (int j = 0; j <= 15; ++j) {			if ((j == n[0]) || (j == n[1]) || (j == n[2]) || (j == n[3]) || (j == n[4]) || (j == n[5]) || (j == n[6])					|| (j == n[7])|| (j == n[8]) || (j == n[9]) || (j == n[10]) || (j == n[11]) || (j == n[12])					|| (j == n[13]) || (j == n[14]) ) {			} else {				return j;			}		}		return -1;	} }

**（4） 地狱难度的游戏界面**

    import java.util.Random; import javafx.application.Application;import javafx.event.ActionEvent;import javafx.event.EventHandler;import javafx.geometry.Insets;import javafx.geometry.Pos;import javafx.geometry.Rectangle2D;import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.control.Alert;import javafx.scene.control.Button;import javafx.scene.control.Alert.AlertType;import javafx.scene.image.Image;import javafx.scene.image.ImageView;import javafx.scene.input.MouseEvent;import javafx.scene.layout.GridPane;import javafx.scene.layout.HBox;import javafx.scene.layout.VBox;/***游戏界面----困难*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class Game_3 extends Application {	public int m; // m是不在随机数组的那个数字	ImageView[] imageViews = new ImageView[25]; 	@Override	public void start(Stage primaryStage) {		init(primaryStage); 	} 	public void init(Stage primaryStage) {		// 父布局		VBox vBox = new VBox(); 		// 3*3九宫格布局，作为上方的选项嵌套入父布局		GridPane gridPane = new GridPane(); 		// 水平布局，作为下方的选项嵌套入父布局		HBox hbox = new HBox();		hbox.setPadding(new Insets(10)); // 填充		hbox.setAlignment(Pos.CENTER); // 居中 		// 添加3个点击		Button home = new Button("返回首页");		home.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即首页窗口				Start start = new Start();				start.start(new Stage());				// 关闭原本界面				primaryStage.close();			}		});		Button again = new Button("重新游戏");		again.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即游戏窗口				Game_3 game = new Game_3();				game.start(new Stage());				// 关闭开始界面				primaryStage.close();			}		});		Button look = new Button("查看原图");		look.setOnAction(new EventHandler<ActionEvent>() {			@Override			public void handle(ActionEvent arg0) {				// 打开另一个窗口，即显示原图				OnImage_3 OnImage = new OnImage_3();				OnImage.start(new Stage());			}		});		// 设置按钮大小并居中		home.setPrefSize(200, 50);		again.setPrefSize(200, 50);		look.setPrefSize(200, 50);		// 设置控件之间的距离		hbox.setSpacing(100); 		hbox.getChildren().addAll(home, again, look); 		// 游戏部分		/*		 * 自定义的函数，产生逆序数为偶数的不重复数组,依次作为图片数组的下标，例如: 2 0 1 3 4 5 6 7 ------>，此时m=8,变成如下即为正确：		 * 0 1 2 3 4 5 4 7		 */		int[] n = random(); 		Image image2 = new Image("application/2_2.jpg"); 		for (int i = 0; i < 25; i++) {			imageViews[i] = new ImageView(image2); // 初始化数组			imageViews[i].setOnMouseClicked(new myevent()); // 设置点击事件		}		for (int i = 0, k = 0; i <= 4; i++) {			for (int j = 0; j <= 4; j++, k++) {				imageViews[k].setViewport(new Rectangle2D(125 * j, 125 * i, 125, 125)); // 切割图片分配给图片数组			}		}		// 按照产生的随机数将imageView数组加入面板		gridPane.add(imageViews[n[0]], 0, 0);		gridPane.add(imageViews[n[1]], 1, 0);		gridPane.add(imageViews[n[2]], 2, 0);		gridPane.add(imageViews[n[3]], 3, 0);		gridPane.add(imageViews[n[4]], 4, 0);		gridPane.add(imageViews[n[5]], 0, 1);		gridPane.add(imageViews[n[6]], 1, 1);		gridPane.add(imageViews[n[7]], 2, 1);		gridPane.add(imageViews[n[8]], 3, 1);		gridPane.add(imageViews[n[9]], 4, 1);		gridPane.add(imageViews[n[10]], 0, 2);		gridPane.add(imageViews[n[11]], 1, 2);		gridPane.add(imageViews[n[12]], 2, 2);		gridPane.add(imageViews[n[13]], 3, 2);		gridPane.add(imageViews[n[14]], 4, 2);		gridPane.add(imageViews[n[15]], 0, 3);		gridPane.add(imageViews[n[16]], 1, 3);		gridPane.add(imageViews[n[17]], 2, 3);		gridPane.add(imageViews[n[18]], 3, 3);		gridPane.add(imageViews[n[19]], 4, 3);		gridPane.add(imageViews[n[20]], 0, 4);		gridPane.add(imageViews[n[21]], 1, 4);		gridPane.add(imageViews[n[22]], 2, 4);		gridPane.add(imageViews[n[23]], 3, 4);		m = findnum(n); // 找出那个不在随机数组里面的数字 		Image image1 = new Image("application/3.jpg"); // 3.png为一个透明图，放在空格子中		imageViews[m].setImage(image1);		gridPane.add(imageViews[m], 4, 4);		gridPane.setGridLinesVisible(true);		gridPane.setPrefWidth(800);		gridPane.setPrefHeight(700);		vBox.getChildren().add(gridPane);		// 布局嵌套，选项部分		vBox.getChildren().add(hbox); 		// 标题栏图标		Image image = new Image("application/4.jpg"); 		Scene scene = new Scene(vBox, 800, 800);		scene.getStylesheets().add(getClass().getResource("Game.css").toExternalForm());		primaryStage.getIcons().add(image);		primaryStage.setTitle("智障拼图");		primaryStage.setScene(scene);		primaryStage.setResizable(false);		primaryStage.show();	} 	public int[] random() { // 生成24个不重复的逆序数为偶数的数字,这样拼图才有结		int[] ran = new int[24];		while (iso(ran) == false) {			ran = random_num();		}		return ran; 	} 	public int[] random_num() { // 生成24个不重复数		int r[] = new int[24];		Random random = new Random();		for (int i = 0; i < 24; ++i) {			r[i] = random.nextInt(25);			for (int j = 0; j < i; ++j) {				while (r[i] == r[j]) {					i--;					break;				}			}		}		return r;	} 	// 判断逆序数是否为偶数	public boolean iso(int[] num) {		int sum = 0;		for (int i = 0; i <= 22; ++i) {			for (int j = i; j <= 23; j++) {				if (num[i] > num[j]) {					sum++;				}			}		}		if ((sum % 2) == 0 && sum != 0) {			return true;		} 		return false; 	} 	// 点击事件的实现	class myevent implements EventHandler<MouseEvent> { 		@Override		public void handle(MouseEvent arg0) { 			ImageView img = (ImageView) arg0.getSource();			double sx = img.getLayoutX();			double sy = img.getLayoutY();			double dispx = sx - imageViews[m].getLayoutX();			double dispy = sy - imageViews[m].getLayoutY();			if ((dispx == -125) && (dispy == 0)) { // 点击的空格左边的格子				swapimg(img, imageViews[m]); // 交换imageView				if (issucc(imageViews)) { // 判断是否拼成功					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} 			else if ((dispx == 0) && (dispy == -125)) { // 上面的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} else if ((dispx == 125) && (dispy == 0)) { // 右边的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			} else if ((dispx == 0) && (dispy == 125)) { // 下面的格子				swapimg(img, imageViews[m]);				if (issucc(imageViews)) {					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");					alert.show();				}			}		} 		// 交换两个imageView的实现		public void swapimg(ImageView i1, ImageView i2) {			int row1 = GridPane.getRowIndex(i1);			int colu1 = GridPane.getColumnIndex(i1);			int row2 = GridPane.getRowIndex(i2);			int colu2 = GridPane.getColumnIndex(i2);			GridPane.setRowIndex(i1, row2);			GridPane.setColumnIndex(i1, colu2);			GridPane.setRowIndex(i2, row1);			GridPane.setColumnIndex(i2, colu1);		}	} 	// 判断是否拼图成功	public boolean issucc(ImageView[] imageViews) {		for (int i = 0; i <= 24; ++i) {			if (i != 3 * GridPane.getRowIndex(imageViews[i]) + GridPane.getColumnIndex(imageViews[i])) {				return false;			}		}		return true;	} 	// 找出m	public int findnum(int[] n) {		for (int j = 0; j <= 24; ++j) {			if ((j == n[0]) || (j == n[1]) || (j == n[2]) || (j == n[3]) || (j == n[4]) || (j == n[5]) || (j == n[6])					|| (j == n[7]) || (j == n[8]) || (j == n[9]) || (j == n[10]) || (j == n[11]) || (j == n[12])					|| (j == n[13]) || (j == n[14]) || (j == n[15]) || (j == n[16]) || (j == n[17]) || (j == n[18])					|| (j == n[19]) || (j == n[20]) || (j == n[21]) || (j == n[22]) || (j == n[23])) {			} else {				return j;			}		}		return -1;	} }

**（5）简单难度显示原图界面 **

    import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.image.Image;import javafx.scene.image.ImageView;import javafx.scene.layout.VBox;/***显示原图界面*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class OnImage_1 extends Application { 	@Override	public void start(Stage primaryStage) {		try {			VBox vBox = new VBox();			// 原图			Image image1 = new Image("application/2.jpg");			double width = image1.getWidth();			double higth = image1.getHeight();			ImageView imageView = new ImageView(image1);			vBox.getChildren().add(imageView); 			// 标题栏图标			Image image = new Image("application/4.jpg"); 			Scene scene = new Scene(vBox, width, higth);			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());			primaryStage.getIcons().add(image);			primaryStage.setTitle("智障拼图");			primaryStage.setScene(scene);			primaryStage.setResizable(false);			primaryStage.show();		} catch (Exception e) {			e.printStackTrace();		}	}	}

**（6）困难难度显示原图界面 **

    import javafx.application.Application; import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.image.Image;import javafx.scene.image.ImageView;import javafx.scene.layout.VBox; /***显示原图界面*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class OnImage_2 extends Application { 	@Override	public void start(Stage primaryStage) {		try {			VBox vBox = new VBox();			// 原图			Image image1 = new Image("application/2_1.jpg");			double width = image1.getWidth();			double higth = image1.getHeight();			ImageView imageView = new ImageView(image1);			vBox.getChildren().add(imageView); 			// 标题栏图标			Image image = new Image("application/4.jpg"); 			Scene scene = new Scene(vBox, width, higth);			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());			primaryStage.getIcons().add(image);			primaryStage.setTitle("智障拼图");			primaryStage.setScene(scene);			primaryStage.setResizable(false);			primaryStage.show();		} catch (Exception e) {			e.printStackTrace();		}	}	}

**（7）地狱难度显示原图界面 **

    import javafx.application.Application; import javafx.stage.Stage;import javafx.scene.Scene;import javafx.scene.image.Image;import javafx.scene.image.ImageView;import javafx.scene.layout.VBox; /***显示原图界面*作者：Mr. Yu*2018年12月5日,下午5:40:51 */public class OnImage_3 extends Application { 	@Override	public void start(Stage primaryStage) {		try {			VBox vBox = new VBox();			// 原图			Image image1 = new Image("application/2_2.jpg");			double width = image1.getWidth();			double higth = image1.getHeight();			ImageView imageView = new ImageView(image1);			vBox.getChildren().add(imageView); 			// 标题栏图标			Image image = new Image("application/4.jpg"); 			Scene scene = new Scene(vBox, width, higth);			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());			primaryStage.getIcons().add(image);			primaryStage.setTitle("智障拼图");			primaryStage.setScene(scene);			primaryStage.setResizable(false);			primaryStage.show();		} catch (Exception e) {			e.printStackTrace();		}	}	}

**有几个点需要注意一下：(1)必须要装JAVAFX插件且JDK1.8或以上才可以运行，需要的可以找我提供内嵌了插件的Eclipse安装包**

**                                        (2)我的图片是存放在资源文件中，即在本包中，会被自动拷贝到bin目录下，大家的图片来源可以更换为本地图片或网址图片**

## <a name="t4"></a>**（五）后续**

**现在这个程序还是很简陋的，本来想美化一下界面，再完善一些功能，诸如倒计时，已走步数，精确提示，背景音乐播放，供玩家可选择的拼图图片等等，但是想想自己那么懒还是算了哈哈哈。**

</div>

</div>

</article>

</div>

<script>$(".MathJax").remove(); if ($('div.markdown_views pre.prettyprint code.hljs').length > 0) { $('div.markdown_views')[0].className = 'markdown_views'; }</script>

<div id="dmp_ad_58">

<div id="kp_box_58" data-pid="58" data-track-click="{&quot;mod&quot;:&quot;kp_popu_58-386&quot;,&quot;con&quot;:&quot;,,&quot;}">

<div style="width:100%;background:#fff;">

<div><iframe width="900" frameborder="0" height="104" scrolling="no" src="//pos.baidu.com/s?hei=104&amp;wid=900&amp;di=u3501897&amp;ltu=https%3A%2F%2Fblog.csdn.net%2Fqq_42370146%2Farticle%2Fdetails%2F84842168&amp;psi=a42874e0295e1896750eed6e803c8a8f&amp;dtm=HTML_POST&amp;tcn=1559875409&amp;cmi=4&amp;cdo=-1&amp;par=2048x1112&amp;ltr=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dd28U4k9FmRe4DU1f7GX1BVwvOeHCHj0uMMspuGQbLn2Jl0UjR4AU9AmigoBfe1YZfe8BylFMHNP37tJReSyCMyWDjyQxpfn2Q4ORE0yV-ua%26wd%3D%26eqid%3D955e426a005a80ed000000065cf9cf13&amp;ps=26973.400390625x510&amp;cec=UTF-8&amp;prot=2&amp;tlm=1559875409&amp;exps=111000,119008,110011&amp;cja=false&amp;dai=5&amp;col=en-US&amp;cfv=0&amp;pcs=2031x1042&amp;cce=true&amp;ccd=24&amp;chi=1&amp;cpl=3&amp;pis=-1x-1&amp;ari=2&amp;psr=2048x1152&amp;drs=3&amp;dis=0&amp;tpr=1559875409103&amp;ant=0&amp;ti=%E3%80%90java%E3%80%91JavaFX%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%AE%9E%E7%8E%B0%E6%8B%BC%E5%9B%BE%E5%B0%8F%E6%B8%B8%E6%88%8F%20-%20%E4%BB%A5%E5%90%8E%E6%88%91%E8%A6%81%E5%BD%93%E6%9D%91%E9%95%BF%20-%20CSDN%E5%8D%9A%E5%AE%A2&amp;dc=3&amp;dri=0&amp;pss=2031x34354"></iframe></div>

</div>

</div>

</div>

<a id="commentBox"></a>

<div class="comment-box">

<div class="comment-edit-box d-flex"><a id="commentsedit"></a>

<div class="user-img">[![](https://avatar.csdn.net/6/F/7/3_weixin_44094314.jpg)](//me.csdn.net/weixin_44094314) </div>

<form id="commentform"><input type="hidden" id="comment_replyId"> <textarea class="comment-content" name="comment_content" id="comment_content" placeholder="想对作者说点什么"></textarea>

<div class="opt-box">

<div id="ubbtools" class="add_code">[](#insertcode)</div>

<input type="hidden" id="comment_replyId" name="comment_replyId"> <input type="hidden" id="article_id" name="article_id" value="84842168"> <input type="hidden" id="comment_userId" name="comment_userId" value=""> <input type="hidden" id="commentId" name="commentId" value="">

<div style="display: none;" class="csdn-tracking-statistics tracking-click" data-mod="popu_384">[发表评论](#)</div>

<div class="dropdown" id="myDrap"><a class="dropdown-face d-flex align-items-center" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">

<div class="txt-selected text-truncate">添加代码片</div>

</a>

*   <a data-code="html">HTML/XML</a>
*   <a data-code="objc">objective-c</a>
*   <a data-code="ruby">Ruby</a>
*   <a data-code="php">PHP</a>
*   <a data-code="csharp">C</a>
*   <a data-code="cpp">C++</a>
*   <a data-code="javascript">JavaScript</a>
*   <a data-code="python">Python</a>
*   <a data-code="java">Java</a>
*   <a data-code="css">CSS</a>
*   <a data-code="sql">SQL</a>
*   <a data-code="plain">其它</a>

</div>

<div class="right-box"><span id="tip_comment" class="tip">还能输入_1000_个字符</span> <input type="submit" class="btn btn-sm btn-red btn-comment" value="发表评论"></div>

</div>

</form>

</div>

<div class="comment-list-container"><a id="comments"></a>

<div class="comment-list-box" style="max-height: none;">

*   [![weixin_45075885](https://avatar.csdn.net/0/E/D/3_weixin_45075885.jpg)](https://me.csdn.net/weixin_45075885)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">CLSChenml：</span>](https://me.csdn.net/weixin_45075885) <span class="comment">博主你这个的困难和地狱模式赢了并不会有提示，issue方法里面分别改一下就好</span><span class="date" title="2019-06-04 18:30:25">(2天前</span><span class="floor-num">#7楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9924633"><span></span></div>

    </div>

*   [![weixin_45075885](https://avatar.csdn.net/0/E/D/3_weixin_45075885.jpg)](https://me.csdn.net/weixin_45075885)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">CLSChenml：</span>](https://me.csdn.net/weixin_45075885) <span class="comment">具体的细节我写在博客里了 博主可以看看 https://blog.csdn.net/weixin_45075885/article/details/90764123</span><span class="date" title="2019-06-04 11:06:32">(2天前</span><span class="floor-num">#6楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9920394"><span></span></div>

    </div>

*   [![weixin_45075885](https://avatar.csdn.net/0/E/D/3_weixin_45075885.jpg)](https://me.csdn.net/weixin_45075885)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">CLSChenml：</span>](https://me.csdn.net/weixin_45075885) <span class="comment">不过有一点是，如果下面的三个按钮存在，方向键就会自己去选择按钮，而不是移动图片了。。没办法我只能把按钮都删了，不知道有没有什么好的解决办法</span><span class="date" title="2019-06-04 01:26:45">(3天前</span><span class="floor-num">#5楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9918571"><span></span></div>

    </div>

*   [![weixin_45075885](https://avatar.csdn.net/0/E/D/3_weixin_45075885.jpg)](https://me.csdn.net/weixin_45075885)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">CLSChenml：</span>](https://me.csdn.net/weixin_45075885)<span class="comment">

    <pre name="code2" class="java hljs">

    2.  <div class="hljs-ln-code">

        <div class="hljs-ln-line">`<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myKeyEvent</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">EventHandler</span><<span class="hljs-title">KeyEvent</span>></span> {`</div>

        </div>

    4.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-meta">@Override</span>`</div>

        </div>

    5.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handle</span><span class="hljs-params">(KeyEvent arg0)</span></span> {`</div>

        </div>

    7.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span>[][] ncopy4 = ncopy3;`</div>

        </div>

    8.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `myevent myevent1 = <span class="hljs-keyword">new</span> myevent();`</div>

        </div>

    9.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> mrow = GridPane.getRowIndex(imageViews[m]);`</div>

        </div>

    10.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> mcol = GridPane.getColumnIndex(imageViews[m]);`</div>

        </div>

    11.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> mindex = mrow * <span class="hljs-number">3</span> + mcol;`</div>

        </div>

    13.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">// 针对不同的按键给出不同的反应</span>`</div>

        </div>

    14.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">switch</span> (arg0.getCode()) {`</div>

        </div>

    15.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">case</span> DOWN:`</div>

        </div>

    16.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">// 计算出需要交换的对象图片的位置nindex</span>`</div>

        </div>

    17.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> nrow = mrow + <span class="hljs-number">1</span>;`</div>

        </div>

    18.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> ncol = mcol;`</div>

        </div>

    19.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> nindex = nrow * <span class="hljs-number">3</span> + ncol;`</div>

        </div>

    20.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">if</span> (nindex >= <span class="hljs-number">0</span> && nindex &lt;= <span class="hljs-number">8</span>) {`</div>

        </div>

    21.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">// 由于n[]中的索引是和位置一一对应的，再将其值作为imageViews的索引</span>`</div>

        </div>

    22.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">// 只要算出nindex，就能对应上相应的图片。将其交换</span>`</div>

        </div>

    23.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">// ncopy3是一个2*9的二维数组，n[]的八个元素在前，m在最后一位。第二行为0到8。</span>`</div>

        </div>

    24.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `myevent1.swapimg(imageViews[m], imageViews[ncopy3[<span class="hljs-number">0</span>][ncopy3[<span class="hljs-number">1</span>][nindex]]]);`</div>

        </div>

    25.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">// 图片交换后，将第一行中的值也交换，否则多次操作之后数据会混乱，导致胡乱交换。第二行不变(代表地址)。</span>`</div>

        </div>

    26.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">int</span> temp2 = ncopy3[<span class="hljs-number">0</span>][mindex];`</div>

        </div>

    27.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `ncopy3[<span class="hljs-number">0</span>][mindex] = ncopy3[<span class="hljs-number">0</span>][nindex];`</div>

        </div>

    28.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `ncopy3[<span class="hljs-number">0</span>][nindex] = temp2;`</div>

        </div>

    29.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `}`</div>

        </div>

    30.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">break</span>;`</div>

        </div>

    31.  <div class="hljs-ln-code">

        <div class="hljs-ln-line">`………………`</div>

        </div>

    </pre>

    </span><span class="date" title="2019-06-04 00:44:24">(3天前</span><span class="floor-num">#4楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9918508"><span></span></div>

    </div>

*   [![weixin_45075885](https://avatar.csdn.net/0/E/D/3_weixin_45075885.jpg)](https://me.csdn.net/weixin_45075885)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">CLSChenml：</span>](https://me.csdn.net/weixin_45075885) <span class="comment">感谢博主！我在你的基础上添加了键盘操作，就是上下左右！搞了我一整天，因为gridpane不支持通过坐标返回源… 先通过getcol和getrow获取坐标，然后算出上下左右的坐标，最坑爹的就是知道了座标却不能直接提取，因此就不能直接交换！然后参考了你判断拼好的思路，发现n[]这个随机数组中值虽然是随机的，但是n[1],n[2]却是依次排列的，比如imageview[n[5]]就代表第5张图，这样就可以实现交换了。 但是交换过去后有一个很严重的问题，就是把第九张图和第六张图交换之后想再换回去时，现在空白方块在地址5，通过计算下面的方块地址为8，应该和n[8]交换，但是n[8]其实还是刚刚的第九张图，因此就会一直和自己交换，程序看上去就一动不动。这点我想了一个晚上，最后的办法是用一个二维数组ncopy，第一行拷贝n[],第二行从0到8，代表地址。在交换的时候就直接从二维数组的第二行中提取myevent1.swapimg(imageViews[m], imageViews[ncopy3[0][ncopy3[1][nindex]]]);，不是简单的访问一维的索引,然后在交换图片之后把第0行的两个元素也随之交换，这样图片交换过去了，值也交换过去了，而计算出来的地址却没有发生变动。 代码我在下面贴出来，请斧正！</span><span class="date" title="2019-06-04 00:38:43">(3天前</span><span class="floor-num">#3楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9918488"><span></span></div>

    </div>

*   [![RS584521](https://avatar.csdn.net/9/9/E/3_rs584521.jpg)](https://me.csdn.net/RS584521)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">小鱼人Dream：</span>](https://me.csdn.net/RS584521) <span class="comment">你这没问题吗？，为什么我展示的切割之后的图片会有重复的？而且点击交换图片，变化也会有问题，。。。。。求解答。。</span><span class="date" title="2019-01-11 17:37:57">(4个月前</span><span class="floor-num">#2楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-read-reply" data-type="readreply">查看回复(4)</a><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9033659"><span></span></div>

    </div>

*   *   [![RS584521](https://avatar.csdn.net/9/9/E/3_rs584521.jpg)](https://me.csdn.net/RS584521)

        <div class="right-box reply-box">

        <div class="info-box">[<span class="name mr-8">小鱼人Dream</span>](https://me.csdn.net/RS584521)<span class="text">回复</span> <span class="name">以后我要当村长：</span> <span class="comment">[code=java] Image image = new Image("1.jpg"); GridPane gridPane = new GridPane(); for(int i = 0, k = 0; i &lt;= 2; ++i) { for(int j = 0; j &lt;= 2; ++j, ++k) { imageViews[k] = new ImageView(image); //初始化数组 imageViews[k].setOnMouseClicked(new myevent()); //设置点击事件 imageViews[k].setViewport(new Rectangle2D(100 * j, 100 * i, 100, 100)); //切割图片 //System.out.println(imageViews[k] + "----" + 100 * j + ":" + 100 * i); } } gridPane.add(imageViews[0], 0, 0); //按照产生的随机数将imageView数组加入面板 gridPane.add(imageViews[1], 0, 1); gridPane.add(imageViews[2], 0, 2); gridPane.add(imageViews[3], 1, 0); gridPane.add(imageViews[4], 1, 1); gridPane.add(imageViews[5], 1, 2); gridPane.add(imageViews[6], 2, 0); gridPane.add(imageViews[7], 2, 1); gridPane.add(imageVie</span><span class="date" title="2019-01-25 15:49:53">(4个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="9105063"><span></span></div>

        </div>

    *   [![RS584521](https://avatar.csdn.net/9/9/E/3_rs584521.jpg)](https://me.csdn.net/RS584521)

        <div class="right-box reply-box">

        <div class="info-box">[<span class="name mr-8">小鱼人Dream</span>](https://me.csdn.net/RS584521)<span class="text">回复</span> <span class="name">以后我要当村长：</span> <span class="comment">不是切割问题，代码我当然改了，没法贴图评论，这个问题是很怪异的，假如我启动，所以图片都不重复，然后我点击开始拼图，拼图的过程中，图片变化就出错了，出现了重复的图片，但是实际上图片是并不重复的，后来实验证实跟图片的坐标有关系，就是gridPane的x,y坐标有关系，但是为什么会出现这样的问题就不得而知了，所以也没法解决，后来我换了用流去切割图片，换成另一种设定坐标的方式就没有这种问题了；你可以直接测试一下，用new Rectangle2D直接切割一张图片，然后按顺序把切割之后的图片放到gridPane中，看能不能组成原图，你就知道我描述的问题是什么了，我把一张图片300*300的图片切割成9份，我单独的显示每一份，都不重复，但是你把他们一起放入到gridPane中，他们就会造成重复，前提放入的坐标是不冲突的，但是还是会重复，不知道为什么你没遇到这种问题？希望你能为我解惑，或者是我忽略了哪里的问题造成的？求解答</span><span class="date" title="2019-01-25 15:49:21">(4个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="9105060"><span></span></div>

        </div>

    *   [![qq_42370146](https://avatar.csdn.net/B/E/7/3_qq_42370146.jpg)](https://me.csdn.net/qq_42370146)

        <div class="right-box reply-box">

        <div class="info-box">[<span class="name mr-8">以后我要当村长</span>](https://me.csdn.net/qq_42370146)<span class="text">回复</span> <span class="name">以后我要当村长：</span> <span class="comment">还有交换图片方法那儿也要根据你的图片大小进行参数的修改~~~~</span><span class="date" title="2019-01-24 22:02:59">(4个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="9101947"><span></span></div>

        </div>

    *   [![qq_42370146](https://avatar.csdn.net/B/E/7/3_qq_42370146.jpg)](https://me.csdn.net/qq_42370146)

        <div class="right-box reply-box">

        <div class="info-box">[<span class="name mr-8">以后我要当村长</span>](https://me.csdn.net/qq_42370146)<span class="text">回复</span> <span class="name">小鱼人Dream：</span> <span class="comment">注意切割图片的时候，要按照你的图片大小设置切割图片的方法参数，不然会切割重复或者缺漏，直接套代码当然不行啦</span><span class="date" title="2019-01-24 21:53:12">(4个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="9101906"><span></span></div>

        </div>

*   [![weixin_43993465](https://avatar.csdn.net/F/2/C/3_weixin_43993465.jpg)](https://me.csdn.net/weixin_43993465)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">A凉城：</span>](https://me.csdn.net/weixin_43993465) <span class="comment">万长高楼平地起，加油小兄弟</span><span class="date" title="2018-12-06 14:45:29">(6个月前</span><span class="floor-num">#1楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-read-reply" data-type="readreply">查看回复(1)</a><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="8829009"><span></span></div>

    </div>

*   *   [![qq_42370146](https://avatar.csdn.net/B/E/7/3_qq_42370146.jpg)](https://me.csdn.net/qq_42370146)

        <div class="right-box ">

        <div class="info-box">[<span class="name mr-8">以后我要当村长</span>](https://me.csdn.net/qq_42370146)<span class="text">回复</span> <span class="name">A凉城：</span> <span class="comment">房子搭好了？这么有空![表情包](//g.csdnimg.cn/static/face/monkey/35.gif)</span><span class="date" title="2018-12-06 14:55:04">(6个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="8829115"><span></span></div>

        </div>

</div>

<div id="commentPage" class="pagination-box d-none" style="display: block;">

<div id="Paging_05022414167720808" class="ui-paging-container">

*   上一页
*   1
*   下一页

</div>

</div>

</div>

</div>

<div class="recommend-box">

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36812792/article/details/89038527,BlogCommendFromThirdServiceAll_0&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _java_Swing做数字_拼图__小游戏_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">04-05</span> <span class="read-num hover-hide">阅读数 55</span>

</div>

](https://blog.csdn.net/qq_36812792/article/details/89038527 "javaSwing做数字拼图小游戏")

[<span class="desc oneline">移动白块可以将相邻块换掉，最终成功后可以得到这样的结果，并且弹窗显示游戏成功。源码如下：importjava.awt.*;importjava.awt.event.*;importjava.util....</span>](https://blog.csdn.net/qq_36812792/article/details/89038527 "javaSwing做数字拼图小游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">温故而知新</span>](https://blog.csdn.net/qq_36812792)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ranmudaofa/article/details/20842017,BlogCommendFromBaidu_1&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_FX游戏开发--第一课 精灵动画

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-09</span> <span class="read-num hover-hide">阅读数 2694</span>

</div>

](https://blog.csdn.net/ranmudaofa/article/details/20842017 "JavaFX游戏开发--第一课 精灵动画")

[<span class="desc oneline">一直在关注JavaFX的发展，最近想试试使用JavaFX开发游戏是什么样的情况。可惜令我汗颜的是--没有找到类似于Java2D中Graphics/Graphics2D之类的类。自己单纯的继承Node的...</span>](https://blog.csdn.net/ranmudaofa/article/details/20842017 "JavaFX游戏开发--第一课 精灵动画") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">燃木刀法</span>](https://blog.csdn.net/ranmudaofa)</span>

</div>

</div>

<div class="recommend-item-box recommend-download-box clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/qq2442438699/10145248,BlogCommendFromBaidu_2&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _java_fx_实现_雷电游戏

<span class="data float-right">12-04</span></div>

<div class="desc oneline">javafx实现雷电游戏。这是我自己做的程序，用javafx实现的，国内的javafx真的很少，我自己摸索了很久，碰壁挺多的，现在做出了雷电游戏，希望可以帮助那些喜欢javafx的初学者，让他们少碰点</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/qq2442438699/10145248)</div>

<div class="recommend-item-box recommend-download-box clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/ml3947/8091895,BlogCommendFromBaidu_3&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _Java_FX战旗类游戏开发示例

<span class="data float-right">10-28</span></div>

<div class="desc oneline">JavaFX战旗类游戏开发示例，建议结合我的博客文章《JavaFX战旗类游戏开发》来看。该系列七课已完结，有问题可以发我邮件。</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/ml3947/8091895)</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_59" data-pid="59" data-track-click="{&quot;mod&quot;:&quot;kp_popu_59-78&quot;,&quot;con&quot;:&quot;,,&quot;}"><script type="text/javascript">(function() { var s = "_" + Math.random().toString(36).slice(2); document.write('<div style="" id="' + s + '"></div>'); (window.slotbydup = window.slotbydup || []).push({ id: "u3491668", container: s }); })();</script>

<div style="" id="_4n1k0gesyx"><iframe id="iframeu3491668_0" name="iframeu3491668_0" src="https://pos.baidu.com/zchm?conwid=852&amp;conhei=60&amp;rdid=3491668&amp;dc=3&amp;exps=110011&amp;psi=a42874e0295e1896750eed6e803c8a8f&amp;di=u3491668&amp;dri=0&amp;dis=0&amp;dai=1&amp;ps=27046x688&amp;enu=encoding&amp;dcb=___adblockplus&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tsr=0&amp;tpr=1559875395286&amp;ti=%E3%80%90java%E3%80%91JavaFX%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%AE%9E%E7%8E%B0%E6%8B%BC%E5%9B%BE%E5%B0%8F%E6%B8%B8%E6%88%8F%20-%20%E4%BB%A5%E5%90%8E%E6%88%91%E8%A6%81%E5%BD%93%E6%9D%91%E9%95%BF%20-%20CSDN%E5%8D%9A%E5%AE%A2&amp;ari=2&amp;dbv=2&amp;drs=1&amp;pcs=2031x1042&amp;pss=2031x30674&amp;cfv=0&amp;cpl=3&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1559875395&amp;prot=2&amp;rw=1042&amp;ltu=https%3A%2F%2Fblog.csdn.net%2Fqq_42370146%2Farticle%2Fdetails%2F84842168&amp;ltr=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dd28U4k9FmRe4DU1f7GX1BVwvOeHCHj0uMMspuGQbLn2Jl0UjR4AU9AmigoBfe1YZfe8BylFMHNP37tJReSyCMyWDjyQxpfn2Q4ORE0yV-ua%26wd%3D%26eqid%3D955e426a005a80ed000000065cf9cf13&amp;ecd=1&amp;uc=2048x1112&amp;pis=-1x-1&amp;sr=2048x1152&amp;tcn=1559875395&amp;qn=9ad7db407a641e70&amp;dpv=9ad7db407a641e70&amp;tt=1559875395262.30.31.33" width="852" height="60" align="center,center" vspace="0" hspace="0" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" style="border:0;vertical-align:bottom;margin:0;width:852px;height:60px" allowtransparency="true"></iframe></div>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/iteye_14985/article/details/81658143,BlogCommendFromBaidu_4&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 自己编程写的_Java_FX 演示游戏，请大家看看

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-02</span> <span class="read-num hover-hide">阅读数 348</span>

</div>

](https://blog.csdn.net/iteye_14985/article/details/81658143 "自己编程写的JavaFX 演示游戏，请大家看看")

[<span class="desc oneline">2009-05-22：重点推荐JavaFX文章：怎样用JavaFX编写游戏：吃豆人（Pac-Man） 最近读了些JAVAFX的文章，看了一些示范程序，于是决定写个游戏试一试。大概花了2周的业余时间，写...</span>](https://blog.csdn.net/iteye_14985/article/details/81658143 "自己编程写的JavaFX 演示游戏，请大家看看") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">JavaFX Guy的博客</span>](https://blog.csdn.net/iteye_14985)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zzhou12345/article/details/84699121,BlogCommendFromBaidu_5&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _java_fx制作2.5d的rpg游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-29</span> <span class="read-num hover-hide">阅读数 139</span>

</div>

](https://blog.csdn.net/zzhou12345/article/details/84699121 "javafx制作2.5d的rpg游戏 ")

[<span class="desc oneline">之前做的javafx2.5d游戏，现共享出来：精灵八方走astar自动寻路地图滚动小地图剧情对话脚本地图传送地图编辑器简易战斗系统(未完善)原文链接：http://www.zhouhaocheng.c...</span>](https://blog.csdn.net/zzhou12345/article/details/84699121 "javafx制作2.5d的rpg游戏 ") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">java技术博客</span>](https://blog.csdn.net/zzhou12345)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/weixin_39986187/article/details/85078922,BlogCommendClickRateRank_6&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _JAVA_编写_拼图__小游戏_带自动寻路算法

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-18</span> <span class="read-num hover-hide">阅读数 110</span>

</div>

](https://blog.csdn.net/weixin_39986187/article/details/85078922 "JAVA编写拼图小游戏带自动寻路算法")

[<span class="desc oneline">因为课程的关系，要交作业就写了这个小游戏。下面先看看架构对于程序的难点：对于拼图是否存在解的处理：（查到大佬结论）N×N的棋盘，N为奇数时，与八数码问题相同。逆序奇偶同性可互达N为偶数时，空格每上下移...</span>](https://blog.csdn.net/weixin_39986187/article/details/85078922 "JAVA编写拼图小游戏带自动寻路算法") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">咖啡的博客</span>](https://blog.csdn.net/weixin_39986187)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/weixin_34072637/article/details/87417475,BlogCommendClickRateRank_7&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/weixin_34072637/article/details/87417475,BlogCommendClickRateRank_7&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 【开源】发布一个基于_Java_FX的_小游戏_：CrazyAlpha

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-26</span> <span class="read-num hover-hide">阅读数 18</span>

</div>

](https://blog.csdn.net/weixin_34072637/article/details/87417475 "【开源】发布一个基于JavaFX的小游戏：CrazyAlpha")

[<span class="desc oneline">Features基于JavaFX设计了游戏引擎XEngine使用自行开发的游戏引擎XEngine实现完整游戏功能游戏资源管理：字体、图片、音频管理游戏地图管理，多地图切换MVVM分层设计，代码解耦合，...</span>](https://blog.csdn.net/weixin_34072637/article/details/87417475 "【开源】发布一个基于JavaFX的小游戏：CrazyAlpha") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">weixin_34072637的博客</span>](https://blog.csdn.net/weixin_34072637)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/weixin_39056864/article/details/80135238,BlogCommendClickRateRank_8&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/weixin_39056864/article/details/80135238,BlogCommendClickRateRank_8&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_贪吃蛇_小游戏_开发

<div class="info-box d-flex align-content-center">

<span class="date hover-show">04-28</span> <span class="read-num hover-hide">阅读数 411</span>

</div>

](https://blog.csdn.net/weixin_39056864/article/details/80135238 "Java贪吃蛇小游戏开发")

[<span class="desc oneline">1、主要的对象网格（边界）、食物（游戏之一）、蛇（主要对象）、游戏（由网格、食物、蛇组成而有规则的游戏控制）因为食物是由单位网格（一个网格）以及蛇是由几个网格（蛇身）组成的所以将一个网格（一个网格的表...</span>](https://blog.csdn.net/weixin_39056864/article/details/80135238 "Java贪吃蛇小游戏开发") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">liumeifang</span>](https://blog.csdn.net/weixin_39056864)</span>

</div>

</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_60" data-pid="60" data-track-view="{&quot;mod&quot;:&quot;kp_popu_60-894&quot;,&quot;con&quot;:&quot;266590062125636699,https://edu.csdn.net/course/detail/4899,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_60-894&quot;,&quot;con&quot;:&quot;266590062125636699,https://edu.csdn.net/course/detail/4899,&quot;}"><link rel="stylesheet" href="https://www.csdn.net/company/css/edu-recommend-1.0.1.css">

<div class="edu-ad-list">

<div class="recommend-item-box type_blog clearfix">

<div class="content" style="width: 962px;">[

#### 从入门开始学_JAVA_第二章_JAVA_语言基础

](https://edu.csdn.net/course/detail/4899?utm_source=baidutj "从入门开始学<em>JAVA</em>第二章<em>JAVA</em>语言基础")

[<span class="desc oneline">学习JAVA之路的第二章，主要讲解java开发工具eclipse以及Java的一个语言基础以及二进制的一个讲解</span>](https://edu.csdn.net/course/detail/4899?utm_source=baidutj "从入门开始学<em>JAVA</em>第二章<em>JAVA</em>语言基础") <span class="blog_title_box oneline "><span class="type-show type-show-edu type-show-after">学院</span> 讲师： <span class="blog_title">朱祚华</span></span>

</div>

</div>

</div>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/aabbccCPP/article/details/82955473,BlogCommendClickRateRank_9&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/aabbccCPP/article/details/82955473,BlogCommendClickRateRank_9&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _java_代码_实现_24点_小游戏_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-07</span> <span class="read-num hover-hide">阅读数 241</span>

</div>

](https://blog.csdn.net/aabbccCPP/article/details/82955473 "java代码实现24点小游戏")

[<span class="desc oneline">24点游戏是经典的纸牌益智游戏。常见游戏规则：  从扑克中每次取出4张牌。使用加减乘除，第一个能得出24者为赢。（其中，J代表11，Q代表12，K代表13，A代表1），按照要求编程解决24点游戏。基本...</span>](https://blog.csdn.net/aabbccCPP/article/details/82955473 "java代码实现24点小游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">aabbccCPP的博客</span>](https://blog.csdn.net/aabbccCPP)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Wyx_wx/article/details/73555258,BlogCommendClickRateRank_10&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Wyx_wx/article/details/73555258,BlogCommendClickRateRank_10&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _java__实现_简单数独游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-21</span> <span class="read-num hover-hide">阅读数 3760</span>

</div>

](https://blog.csdn.net/Wyx_wx/article/details/73555258 "java实现简单数独游戏")

[<span class="desc oneline">本来打算晚上把javaFx需要的组件装好以后直接用javaFx的，但似乎eclipse的版本不对，安装了也不能用，非洲人非了一天...数独代码是在之前寒假受命写的，学了一个月java的成果，现在看来有...</span>](https://blog.csdn.net/Wyx_wx/article/details/73555258 "java实现简单数独游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">词庸</span>](https://blog.csdn.net/Wyx_wx)</span>

</div>

</div>

<div class="recommend-item-box blog-expert-recommend-box" style="display: block;">

<div class="d-flex">

<div class="blog-expert-recommend">

<div class="blog-expert">

<div class="blog-expert-flexbox" data-track-view="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">

<div class="blog-expert-item">

<div class="blog-expert-info-box">

<div class="blog-expert-img-box" data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[![Yorhom](https://avatar.csdn.net/0/E/4/3_yorhomwang.jpg "Yorhom")](https://blog.csdn.net/yorhomwang)<span data-track-click="{&quot;mod&quot;:&quot;popu_710&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}"><span class="blog-expert-button-follow btn-red-follow" data-name="yorhomwang" data-nick="Yorhom">关注</span></span></div>

<div class="info"><span data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[

##### Yorhom

](https://blog.csdn.net/yorhomwang)</span>

68篇文章

排名:3000+

</div>

</div>

</div>

<div class="blog-expert-item">

<div class="blog-expert-info-box">

<div class="blog-expert-img-box" data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[![56yangyuwei](https://avatar.csdn.net/E/C/4/3_u011774501.jpg "56yangyuwei")](https://blog.csdn.net/u011774501)<span data-track-click="{&quot;mod&quot;:&quot;popu_710&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}"><span class="blog-expert-button-follow btn-red-follow" data-name="u011774501" data-nick="56yangyuwei">关注</span></span></div>

<div class="info"><span data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[

##### 56yangyuwei

](https://blog.csdn.net/u011774501)</span>

0篇文章

排名:千里之外

</div>

</div>

</div>

<div class="blog-expert-item">

<div class="blog-expert-info-box">

<div class="blog-expert-img-box" data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[![Caczhtus](https://avatar.csdn.net/B/F/E/3_calculate23.jpg "Caczhtus")](https://blog.csdn.net/calculate23)<span data-track-click="{&quot;mod&quot;:&quot;popu_710&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}"><span class="blog-expert-button-follow btn-red-follow" data-name="calculate23" data-nick="Caczhtus">关注</span></span></div>

<div class="info"><span data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[

##### Caczhtus

](https://blog.csdn.net/calculate23)</span>

322篇文章

排名:千里之外

</div>

</div>

</div>

<div class="blog-expert-item">

<div class="blog-expert-info-box">

<div class="blog-expert-img-box" data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[![mcp3128](https://avatar.csdn.net/8/F/8/3_mcp3128.jpg "mcp3128")](https://blog.csdn.net/mcp3128)<span data-track-click="{&quot;mod&quot;:&quot;popu_710&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}"><span class="blog-expert-button-follow btn-red-follow" data-name="mcp3128" data-nick="mcp3128">关注</span></span></div>

<div class="info"><span data-track-click="{&quot;mod&quot;:&quot;popu_709&quot;,&quot;con&quot;:&quot;https://blog.csdn.net/qq_42370146/article/details/84842168&quot;}">[

##### mcp3128

](https://blog.csdn.net/mcp3128)</span>

428篇文章

排名:7000+

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/macrobed/article/details/7847196,BlogCommendESEnWordWeight_11&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/macrobed/article/details/7847196,BlogCommendESEnWordWeight_11&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_语言_实现__拼图_游戏源代码

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-09</span> <span class="read-num hover-hide">阅读数 3583</span>

</div>

](https://blog.csdn.net/macrobed/article/details/7847196 "Java语言实现拼图游戏源代码")

[<span class="desc oneline">/* *JAVA小游戏－拼图我做的第一个小游戏 *Cell类是继承的按钮类，并加上相应图形，形成方格 *MyCanvas是一个面板，加载Cell类的对象（方格），是这三个类中的核心 */importj...</span>](https://blog.csdn.net/macrobed/article/details/7847196 "Java语言实现拼图游戏源代码") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">macrobed的专栏</span>](https://blog.csdn.net/macrobed)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/angry_youth/article/details/71404651,BlogCommendESEnWordWeight_12&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/angry_youth/article/details/71404651,BlogCommendESEnWordWeight_12&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _拼图_游戏---_java__实现_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">05-08</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/angry_youth/article/details/71404651 "拼图游戏---java实现")

[<span class="desc oneline">游戏说明：设计一款拼图游戏，要求点击图片按钮，实现图片按钮的移动，直到每一个按钮都到达指定位置游戏终止退出。游戏设计思路：1.准备一张图像文件；2.创建N个按钮图标，每个按钮图标里面存入一张分割后的图...</span>](https://blog.csdn.net/angry_youth/article/details/71404651 "拼图游戏---java实现") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">angry_youth的博客</span>](https://blog.csdn.net/angry_youth)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_31726419/article/details/50571392,BlogCommendESEnWordWeight_13&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_31726419/article/details/50571392,BlogCommendESEnWordWeight_13&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 简易的_Java__拼图_游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-23</span> <span class="read-num hover-hide">阅读数 2553</span>

</div>

](https://blog.csdn.net/qq_31726419/article/details/50571392 "简易的Java拼图游戏")

[<span class="desc oneline">简易的Java拼图游戏,将图片用PS切成4*4,16份，命名为00.gif,01,gif,02.gif.......以此类推。(去掉00.gif,改为一张空白图片)。16个按钮上显示图片，点击按钮后，...</span>](https://blog.csdn.net/qq_31726419/article/details/50571392 "简易的Java拼图游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">lang的飞起的博客</span>](https://blog.csdn.net/qq_31726419)</span>

</div>

</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_61" data-pid="61" data-track-view="{&quot;mod&quot;:&quot;kp_popu_61-622&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_61-622&quot;,&quot;con&quot;:&quot;,,&quot;}">

<div id="_hoasjjy4rpt"><iframe width="852" frameborder="0" height="66" scrolling="no" src="https://pos.baidu.com/s?hei=66&amp;wid=852&amp;di=u3600846&amp;ltu=https%3A%2F%2Fblog.csdn.net%2Fqq_42370146%2Farticle%2Fdetails%2F84842168&amp;psi=a42874e0295e1896750eed6e803c8a8f&amp;drs=3&amp;dc=3&amp;tcn=1559875409&amp;cce=true&amp;cec=UTF-8&amp;ti=%E3%80%90java%E3%80%91JavaFX%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%AE%9E%E7%8E%B0%E6%8B%BC%E5%9B%BE%E5%B0%8F%E6%B8%B8%E6%88%8F%20-%20%E4%BB%A5%E5%90%8E%E6%88%91%E8%A6%81%E5%BD%93%E6%9D%91%E9%95%BF%20-%20CSDN%E5%8D%9A%E5%AE%A2&amp;par=2048x1112&amp;chi=1&amp;exps=111000,119008,110011&amp;dai=6&amp;tpr=1559875409103&amp;cpl=3&amp;ps=28711.400390625x534&amp;tlm=1559875409&amp;dis=0&amp;ari=2&amp;pis=-1x-1&amp;cfv=0&amp;ltr=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dd28U4k9FmRe4DU1f7GX1BVwvOeHCHj0uMMspuGQbLn2Jl0UjR4AU9AmigoBfe1YZfe8BylFMHNP37tJReSyCMyWDjyQxpfn2Q4ORE0yV-ua%26wd%3D%26eqid%3D955e426a005a80ed000000065cf9cf13&amp;cja=false&amp;dtm=HTML_POST&amp;cdo=-1&amp;psr=2048x1152&amp;cmi=4&amp;ccd=24&amp;prot=2&amp;pcs=2031x1042&amp;dri=0&amp;pss=2031x34463&amp;col=en-US&amp;ant=0"></iframe></div>

</div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/shichaosen/1704272,BlogCommendESEnWordWeight_14&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/shichaosen/1704272,BlogCommendESEnWordWeight_14&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _Java_Fx a_拼图_游戏

<span class="data float-right">09-28</span></div>

<div class="desc oneline">大家可以看看， 这事我刚接触JavaFX写的一个DEMO。 共同进步。 拼图游戏，附有效果图。 暂不提供源码。</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/shichaosen/1704272)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/u010408078/5617529,BlogCommendESEnWordWeight_15&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/u010408078/5617529,BlogCommendESEnWordWeight_15&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### 用_Java_编写的_拼图_九宫格游戏

<span class="data float-right">06-20</span></div>

<div class="desc oneline">用java编写的一个九宫格拼图游戏，可以支持键盘操作，并且可以选择所拼的图片，很有趣！</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/u010408078/5617529)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011774501/article/details/84767331,BlogCommendFromQuerySearch_16&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011774501/article/details/84767331,BlogCommendFromQuerySearch_16&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java__实现_小_拼图_游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-27</span> <span class="read-num hover-hide">阅读数 403</span>

</div>

](https://blog.csdn.net/u011774501/article/details/84767331 "Java实现小拼图游戏")

[<span class="desc oneline">今天整理之前的项目，发现了在大二上学期的java课程设计中编写的智能拼图小游戏，觉得有意思，所以打算写篇文章和大伙分享分享。 一、项目功能1）本游戏是一个Java语言的拼图游戏，有一个格子是空的，其他...</span>](https://blog.csdn.net/u011774501/article/details/84767331 "Java实现小拼图游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">u011774501的博客</span>](https://blog.csdn.net/u011774501)</span>

</div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/sinat_36319434/9906755,BlogCommendFromQuerySearch_17&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/sinat_36319434/9906755,BlogCommendFromQuerySearch_17&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _java__实现_简单_拼图_游戏

<span class="data float-right">07-21</span></div>

<div class="desc oneline">java语言实现的简单拼图游戏，提供参考</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/sinat_36319434/9906755)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/lzy_1993/9816192,BlogCommendFromQuerySearch_18&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/lzy_1993/9816192,BlogCommendFromQuerySearch_18&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _java_源码 _拼图__小游戏_

<span class="data float-right">04-17</span></div>

<div class="desc oneline">可切换n关卡,可切换图片,带bgm和音效</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/lzy_1993/9816192)</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_62" data-pid="62" data-track-view="{&quot;mod&quot;:&quot;kp_popu_62-623&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_62-623&quot;,&quot;con&quot;:&quot;,,&quot;}"><script type="text/javascript">(function() { var s = "_" + Math.random().toString(36).slice(2); document.write('<div style="" id="' + s + '"></div>'); (window.slotbydup = window.slotbydup || []).push({ id: "u3600849", container: s }); })();</script>

<div style="" id="_hpy85if8gkk"><iframe id="iframeu3600849_0" name="iframeu3600849_0" src="https://pos.baidu.com/zchm?conwid=852&amp;conhei=66&amp;rdid=3600849&amp;dc=3&amp;exps=110011&amp;psi=a42874e0295e1896750eed6e803c8a8f&amp;di=u3600849&amp;dri=0&amp;dis=0&amp;dai=2&amp;ps=28385x688&amp;enu=encoding&amp;dcb=___adblockplus&amp;dtm=HTML_POST&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tsr=0&amp;tpr=1559875395286&amp;ti=%E3%80%90java%E3%80%91JavaFX%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%AE%9E%E7%8E%B0%E6%8B%BC%E5%9B%BE%E5%B0%8F%E6%B8%B8%E6%88%8F%20-%20%E4%BB%A5%E5%90%8E%E6%88%91%E8%A6%81%E5%BD%93%E6%9D%91%E9%95%BF%20-%20CSDN%E5%8D%9A%E5%AE%A2&amp;ari=2&amp;dbv=2&amp;drs=1&amp;pcs=2031x1042&amp;pss=2031x30734&amp;cfv=0&amp;cpl=3&amp;chi=1&amp;cce=true&amp;cec=UTF-8&amp;tlm=1559875395&amp;prot=2&amp;rw=1042&amp;ltu=https%3A%2F%2Fblog.csdn.net%2Fqq_42370146%2Farticle%2Fdetails%2F84842168&amp;ltr=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dd28U4k9FmRe4DU1f7GX1BVwvOeHCHj0uMMspuGQbLn2Jl0UjR4AU9AmigoBfe1YZfe8BylFMHNP37tJReSyCMyWDjyQxpfn2Q4ORE0yV-ua%26wd%3D%26eqid%3D955e426a005a80ed000000065cf9cf13&amp;ecd=1&amp;uc=2048x1112&amp;pis=-1x-1&amp;sr=2048x1152&amp;tcn=1559875395&amp;qn=27c74623b6c44883&amp;tt=1559875395262.40.41.41" width="852" height="66" align="center,center" vspace="0" hspace="0" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" style="border:0;vertical-align:bottom;margin:0;width:852px;height:66px" allowtransparency="true"></iframe></div>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/calculate23/article/details/81592396,BlogCommendFromQuerySearch_19&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/calculate23/article/details/81592396,BlogCommendFromQuerySearch_19&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_小项目__拼图_游戏_基本功能_实现_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-11</span> <span class="read-num hover-hide">阅读数 882</span>

</div>

](https://blog.csdn.net/calculate23/article/details/81592396 "Java小项目_拼图游戏_基本功能实现")

[<span class="desc oneline">前言利用按钮组件以及图片的嵌入完成基本游戏的搭建，其中按钮事件监听是本代码的难点。以及事先要规划好基本模块，包括游戏的UI窗口、操作模块以及代码逻辑设计。启动代码:packageAPI_UI_拼图游戏...</span>](https://blog.csdn.net/calculate23/article/details/81592396 "Java小项目_拼图游戏_基本功能实现") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Caczhtus</span>](https://blog.csdn.net/calculate23)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_23052951/article/details/50291671,BlogCommendFromBaidu_20&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_23052951/article/details/50291671,BlogCommendFromBaidu_20&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 基于_Java_FX--WJFXGameEngine游戏引擎介绍与进度

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-14</span> <span class="read-num hover-hide">阅读数 740</span>

</div>

](https://blog.csdn.net/qq_23052951/article/details/50291671 "基于JavaFX--WJFXGameEngine游戏引擎介绍与进度")

[<span class="desc oneline">计划进行JavaFX的游戏引擎开发已经许久了，但是因为笔记本的数据丢失，导致以前写的代码都不见了。最近开始动笔的时候也不过是4月中旬而已。代码量并不是很多，但是目前基本上雏形已经出来了。也差不多实现了...</span>](https://blog.csdn.net/qq_23052951/article/details/50291671 "基于JavaFX--WJFXGameEngine游戏引擎介绍与进度") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">曾传东的博客</span>](https://blog.csdn.net/qq_23052951)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/awjzb/article/details/50077109,BlogCommendFromBaidu_21&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/awjzb/article/details/50077109,BlogCommendFromBaidu_21&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 使用_Java_Fx_实现__拼图_游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-28</span> <span class="read-num hover-hide">阅读数 3386</span>

</div>

](https://blog.csdn.net/awjzb/article/details/50077109 "使用JavaFx实现拼图游戏")

[<span class="desc oneline">最近学习JavaFx，发现网上大概只有官方文档可以查阅，学习资料较少，写个拼图游戏供记录。。大概说一下思路：1.面板的构建：面板采用GridPane，方便3*3的图片布局。2.每个小格子中的图片当然不...</span>](https://blog.csdn.net/awjzb/article/details/50077109 "使用JavaFx实现拼图游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">awjzb的博客</span>](https://blog.csdn.net/awjzb)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Mingho_Kwok/article/details/81028542,BlogCommendFromBaidu_22&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Mingho_Kwok/article/details/81028542,BlogCommendFromBaidu_22&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_FX _实现_打地鼠游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-13</span> <span class="read-num hover-hide">阅读数 175</span>

</div>

](https://blog.csdn.net/Mingho_Kwok/article/details/81028542 "JavaFX 实现打地鼠游戏")

[<span class="desc oneline">//importjavafx.animation.Animation;importjavafx.animation.PathTransition;importjavafx.animation.Fade...</span>](https://blog.csdn.net/Mingho_Kwok/article/details/81028542 "JavaFX 实现打地鼠游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Mingho_Kwok的博客</span>](https://blog.csdn.net/Mingho_Kwok)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ml3947/article/details/38228749,BlogCommendFromBaidu_23&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ml3947/article/details/38228749,BlogCommendFromBaidu_23&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_FX战旗类游戏开发 第一课 概述

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-28</span> <span class="read-num hover-hide">阅读数 4234</span>

</div>

](https://blog.csdn.net/ml3947/article/details/38228749 "JavaFX战旗类游戏开发 第一课 概述")

[<span class="desc oneline">用JavaFX开发的地图编辑器</span>](https://blog.csdn.net/ml3947/article/details/38228749 "JavaFX战旗类游戏开发 第一课 概述") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Wing的博客</span>](https://blog.csdn.net/ml3947)</span>

</div>

</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_63" data-pid="63" data-track-view="{&quot;mod&quot;:&quot;kp_popu_63-1059&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_63-1059&quot;,&quot;con&quot;:&quot;,,&quot;}"><iframe src="https://kunpeng-sc.csdnimg.cn/#/preview/234?positionId=63&amp;queryWord=" frameborder="0" width="100%" height="75px" scrolling="no"></iframe></div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u010592415/article/details/39450521,BlogCommendFromBaidu_24&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u010592415/article/details/39450521,BlogCommendFromBaidu_24&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_FX-卡牌游戏-Seven Wonders

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-21</span> <span class="read-num hover-hide">阅读数 1835</span>

</div>

](https://blog.csdn.net/u010592415/article/details/39450521 "JavaFX-卡牌游戏-Seven Wonders")

[<span class="desc oneline">用JavaFX写的德式卡牌游戏-SevenWonders,目前还是试行版.自己的游戏之作</span>](https://blog.csdn.net/u010592415/article/details/39450521 "JavaFX-卡牌游戏-Seven Wonders") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Lane_L</span>](https://blog.csdn.net/u010592415)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_23489303/article/details/83994969,BlogCommendClickRateRank_25&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_23489303/article/details/83994969,BlogCommendClickRateRank_25&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 基于_java_FX2的GUI开发

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-12</span> <span class="read-num hover-hide">阅读数 175</span>

</div>

](https://blog.csdn.net/qq_23489303/article/details/83994969 "基于javaFX2的GUI开发")

[<span class="desc oneline">开发工具准备JavaFXSceneBuilder2.0，idea打开idea，新建工程新建后工程结构说明：main为入口函数，sample.fxml就是窗口布局，类似android的xml页面布局。c...</span>](https://blog.csdn.net/qq_23489303/article/details/83994969 "基于javaFX2的GUI开发") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">星耀的博客</span>](https://blog.csdn.net/qq_23489303)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ml3947/article/details/8634475,BlogCommendClickRateRank_26&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ml3947/article/details/8634475,BlogCommendClickRateRank_26&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_ FX即将支持3D了！！

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-04</span> <span class="read-num hover-hide">阅读数 2990</span>

</div>

](https://blog.csdn.net/ml3947/article/details/8634475 "Java FX即将支持3D了！！")

[<span class="desc oneline">虽然工作在进行Android开发，但是在项目业余的时间里，我都在进行Unity3d的学习。也制作了一个联机的坦克对战游戏。而在晚上有时间的时候，也只是在Macmini上学习IOS的开发，所以没怎么写博...</span>](https://blog.csdn.net/ml3947/article/details/8634475 "Java FX即将支持3D了！！") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Wing的博客</span>](https://blog.csdn.net/ml3947)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xiamiflying/article/details/83833486,BlogCommendClickRateRank_27&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xiamiflying/article/details/83833486,BlogCommendClickRateRank_27&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java__实现_贪吃蛇_小游戏_（附完整源码）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-07</span> <span class="read-num hover-hide">阅读数 646</span>

</div>

](https://blog.csdn.net/xiamiflying/article/details/83833486 "Java实现贪吃蛇小游戏（附完整源码）")

[<span class="desc oneline">今天我就从零开始来完成这个小游戏，完成的方式也是一步一步的添加功能这样的方式来实现。第一步完成的功能：写一个界面大家见到的贪吃蛇小游戏，界面肯定是少不了的。因此，第一步就是写一个小界面。实现代码如下：...</span>](https://blog.csdn.net/xiamiflying/article/details/83833486 "Java实现贪吃蛇小游戏（附完整源码）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">javafirst</span>](https://blog.csdn.net/xiamiflying)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011628281/article/details/18743269,BlogCommendClickRateRank_28&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011628281/article/details/18743269,BlogCommendClickRateRank_28&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 【教程1】_Java_制作国际象棋_小游戏_-01

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-24</span> <span class="read-num hover-hide">阅读数 3932</span>

</div>

](https://blog.csdn.net/u011628281/article/details/18743269 "【教程1】Java制作国际象棋小游戏-01")

[<span class="desc oneline">Java制作国际象棋小游戏-01  菜鸟学了几天Java之后手痒痒了，所以开始谋划写个小游戏什么的练练手，刚好一门面向对象的课程布置了一个project，不限内容不限语言，所以菜鸟的小组决定做个国际象...</span>](https://blog.csdn.net/u011628281/article/details/18743269 "【教程1】Java制作国际象棋小游戏-01") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">菜鸟学CS</span>](https://blog.csdn.net/u011628281)</span>

</div>

</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_64" data-pid="64" data-track-view="{&quot;mod&quot;:&quot;kp_popu_64-1060&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_64-1060&quot;,&quot;con&quot;:&quot;,,&quot;}"><iframe src="https://kunpeng-sc.csdnimg.cn/#/preview/235?positionId=64&amp;queryWord=" frameborder="0" width="100%" height="75px" scrolling="no"></iframe></div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/destiny19960207/9763750,BlogCommendClickRateRank_29&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/destiny19960207/9763750,BlogCommendClickRateRank_29&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _Java_开发的游戏 贪吃蛇 完整源代码

<span class="data float-right">02-25</span></div>

<div class="desc oneline">Java开发的游戏 贪吃蛇 的完整代码</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/destiny19960207/9763750)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/mcp3128/10159766,BlogCommendFromQuerySearch_30&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/mcp3128/10159766,BlogCommendFromQuerySearch_30&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### 用_java_编写_拼图__小游戏_

<span class="data float-right">12-15</span></div>

<div class="desc oneline">此程序为用JAVA编写的拼图小游戏，可通过简单的图片移动实现拼图，并实现音乐播放功能。</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/mcp3128/10159766)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/mcp3128/article/details/78798682,BlogCommendFromQuerySearch_31&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/mcp3128/article/details/78798682,BlogCommendFromQuerySearch_31&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_ 简单_拼图_游戏（_实现_音乐播放功能）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-14</span> <span class="read-num hover-hide">阅读数 1820</span>

</div>

](https://blog.csdn.net/mcp3128/article/details/78798682 "Java 简单拼图游戏（实现音乐播放功能）")

[<span class="desc oneline">此程序为用JAVA编写的拼图小游戏，可通过简单的图片移动实现拼图，并实现音乐播放功能。（此程序只完成简单功能的实现，大佬勿喷）软件系统实现拼图主体为一方形区域，位于中央，其中包含九个小区域，放置图片，...</span>](https://blog.csdn.net/mcp3128/article/details/78798682 "Java 简单拼图游戏（实现音乐播放功能）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">mcp3128</span>](https://blog.csdn.net/mcp3128)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/cping1982/article/details/1828037,BlogCommendFromQuerySearch_32&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/cping1982/article/details/1828037,BlogCommendFromQuerySearch_32&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _JAVA__实现__拼图_游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-16</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/cping1982/article/details/1828037 "JAVA实现拼图游戏")

[<span class="desc oneline">package org.test;/** * Title: LoonFramework * Description:拼图图像处理[未优化]（优化算法已内置于loonframework-game框架中。...</span>](https://blog.csdn.net/cping1982/article/details/1828037 "JAVA实现拼图游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">【Java究竟怎么玩?】</span>](https://blog.csdn.net/cping1982)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_42855293/article/details/85947708,BlogCommendFromQuerySearch_33&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_42855293/article/details/85947708,BlogCommendFromQuerySearch_33&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 经典_小游戏_开发思路和算法之_拼图_（1）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-06</span> <span class="read-num hover-hide">阅读数 4319</span>

</div>

](https://blog.csdn.net/qq_42855293/article/details/85947708 "经典小游戏开发思路和算法之拼图（1）")

[<span class="desc oneline">此次开发小游戏一共有18个经典小游戏，每天更新一个。跟大家一起学习一些经典小游戏的开发思路和算法，如果想直接看完整游戏效果的，相关的完整工程可以直接去我的资源里面下载。与大家一起学习Oneday.今天...</span>](https://blog.csdn.net/qq_42855293/article/details/85947708 "经典小游戏开发思路和算法之拼图（1）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">qq_42855293的博客</span>](https://blog.csdn.net/qq_42855293)</span>

</div>

</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_65" data-pid="65" data-track-view="{&quot;mod&quot;:&quot;kp_popu_65-1061&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_65-1061&quot;,&quot;con&quot;:&quot;,,&quot;}"><iframe src="https://kunpeng-sc.csdnimg.cn/#/preview/236?positionId=65&amp;queryWord=" frameborder="0" width="100%" height="75px" scrolling="no"></iframe></div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/lilihuizjy/10027222,BlogCommendFromQuerySearch_34&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/lilihuizjy/10027222,BlogCommendFromQuerySearch_34&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _JAVA_版_拼图_游戏源代码

<span class="data float-right">10-18</span></div>

<div class="desc oneline">这是一个用JAVA语言写的拼图游戏源代码，游戏提供了3*3、4*4、5*5这三种难度等级，同时提供了四张图片供玩家选择，本游戏还提提供了倒计时功能，并且可以将历史游戏玩家所花的时间保存到数据库里。本游戏涉及到JAVA基础、SWING、多线...</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/lilihuizjy/10027222)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ml3947/article/details/38232759,BlogCommendFromBaidu_35&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ml3947/article/details/38232759,BlogCommendFromBaidu_35&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _Java_FX战旗类游戏开发 第三课 创建游戏角色

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-28</span> <span class="read-num hover-hide">阅读数 3177</span>

</div>

](https://blog.csdn.net/ml3947/article/details/38232759 "JavaFX战旗类游戏开发 第三课 创建游戏角色")

[<span class="desc oneline">在上一节课程中，我们学习了在JavaFX中绘制游戏地图。这一节课，我们将会创建我们的游戏角色。 首先，同样的，我们创建一个简单的基类。  importjavafx.scene.canvas.Graph...</span>](https://blog.csdn.net/ml3947/article/details/38232759 "JavaFX战旗类游戏开发 第三课 创建游戏角色") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Wing的博客</span>](https://blog.csdn.net/ml3947)</span>

</div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-other-item-box" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,http://ask.csdn.net/questions/381330,BlogCommendFromBaidu_36&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,http://ask.csdn.net/questions/381330,BlogCommendFromBaidu_36&quot;}" data-flg="true">[

#### _Java_FX小球碰撞检测相关问题

<div class="info-box d-flex align-content-center"><span class="date">04-26</span></div>

<span class="desc oneline">-</span> <span class="type-show type-show-ask">问答</span>

](http://ask.csdn.net/questions/381330)</div>

<div class="recommend-item-box recommend-box-ident recommend-other-item-box" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://bbs.csdn.net/topics/392449859,BlogCommendFromBaidu_37&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://bbs.csdn.net/topics/392449859,BlogCommendFromBaidu_37&quot;}" data-flg="true">[

#### _java_FX写的推箱子_小游戏_下载

<div class="info-box d-flex align-content-center"><span class="date">09-18</span></div>

<span class="desc oneline">使用Java语言实现的推箱子小游戏源码，javaFX生成的界面，逻辑简单明了，都在代码里注释了，运行效果请看：https://blog.csdn.net/qq_40087987/article/det</span> <span class="type-show type-show-bbs">论坛</span>

](https://bbs.csdn.net/topics/392449859)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/meimei881013/2230028,BlogCommendFromBaidu_38&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/meimei881013/2230028,BlogCommendFromBaidu_38&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### _Java_FX_小游戏_编程含源代码！

<span class="data float-right">04-12</span></div>

<div class="desc oneline">这是一个利用javaFX编写的一个小游戏，里面的内容是本人为了打好精神，才那样写的，如有不妥之处还情见谅，谢谢合作！</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/meimei881013/2230028)</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_66" data-pid="66" data-track-view="{&quot;mod&quot;:&quot;kp_popu_66-87&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_66-87&quot;,&quot;con&quot;:&quot;,,&quot;}"><script>NEWS_FEED({ w: 852, h : 60, showid : 'Afihld', placeholderId: "three_ad38", inject : 'define', define : { imagePosition : 'left', imageBorderRadius : 3, imageWidth: 90, imageHeight: 60, imageFill : 'clip', displayImage : true, displayTitle : true, titleFontSize: 18, titleFontColor: '#000', titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif', titleFontWeight: 'bold', titlePaddingTop : 0, titlePaddingRight : 0, titlePaddingBottom : 5, titlePaddingLeft : 16, displayDesc : true, descFontSize: 14, descFontColor: '#8e959a', descFontFamily : 'Microsoft Yahei', paddingTop : 0, paddingRight : 0, paddingBottom : 0, paddingLeft : 0, backgroundColor: '#fff', hoverColor: '#000' } })</script></div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/shaojunxiong/article/details/83265099,BlogCommendFromBaidu_39&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/shaojunxiong/article/details/83265099,BlogCommendFromBaidu_39&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 用_Java_Fx开发一个_小游戏_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-12</span> <span class="read-num hover-hide">阅读数 449</span>

</div>

](https://blog.csdn.net/shaojunxiong/article/details/83265099 "用JavaFx开发一个小游戏")

[<span class="desc oneline">老婆特喜欢一个叫做ColorLinez的小游戏，但这个叫做WinLinez的小游戏的界面实在太老了，而且很多老婆大人想要的功能都没有，因此我一直想给老婆亲手做一个，她想要的，谁让咱是程序员呢？我目前在...</span>](https://blog.csdn.net/shaojunxiong/article/details/83265099 "用JavaFx开发一个小游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">meatloaf</span>](https://blog.csdn.net/shaojunxiong)</span>

</div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/wjzsp25/10683743,BlogCommendClickRateRank_40&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/wjzsp25/10683743,BlogCommendClickRateRank_40&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### 简单贪吃蛇源码

<span class="data float-right">09-23</span></div>

<div class="desc oneline">c语言简单贪吃蛇源码，互相学习，仅限参考，不喜勿喷</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/wjzsp25/10683743)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/zhuaran/2951988,BlogCommendClickRateRank_41&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/zhuaran/2951988,BlogCommendClickRateRank_41&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### 基于_Java_ ＧＵＩ编写的２１点_小游戏_

<span class="data float-right">12-31</span></div>

<div class="desc oneline">基于Java ＧＵＩ编写的２１点小游戏，该游戏代码虽然不是很难，但也不是一时半会能写出来的，可以做为学习交流之用！</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/zhuaran/2951988)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/baidu_28995151/10711427,BlogCommendClickRateRank_42&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/baidu_28995151/10711427,BlogCommendClickRateRank_42&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### 测试记忆力位置的_小游戏_

<span class="data float-right">10-10</span></div>

<div class="desc oneline">javafx编写的一个测试记忆力的小游戏 大概不到80行代码</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/baidu_28995151/10711427)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/s33126521/4148457,BlogCommendClickRateRank_43&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/s33126521/4148457,BlogCommendClickRateRank_43&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### 自制基于_java_FX与JBox2D的音乐游戏

<span class="data float-right">03-17</span></div>

<div class="desc oneline">自制基于javaFX与JBox2D的音乐游戏</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/s33126521/4148457)</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_67" data-pid="67" data-track-view="{&quot;mod&quot;:&quot;kp_popu_67-653&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_67-653&quot;,&quot;con&quot;:&quot;,,&quot;}"><script>NEWS_FEED({ w: 900, h : 84, showid : '9gAEHz', placeholderId: "three_ad43", inject : 'define', define : { imagePosition : 'left', imageBorderRadius : 3, imageWidth: 90, imageHeight: 60, imageFill : 'clip', displayImage : true, displayTitle : true, titleFontSize: 16, titleFontColor: '#000', titleFontFamily : 'Microsoft Yahei', titleFontWeight: 'bold', titlePaddingTop : 0, titlePaddingRight : 0, titlePaddingBottom : 5, titlePaddingLeft : 16, displayDesc : true, descFontSize: 12, descFontColor: '#8e959a', descFontFamily : 'Microsoft Yahei', paddingTop : 10, paddingRight : 0, paddingBottom : 0, paddingLeft : 0, backgroundColor: '#fff', hoverColor: '#000' } })</script></div>

</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_42370146/article/details/86760011,searchFromBaidu1_0,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_42370146/article/details/86760011,searchFromBaidu1_0,-&quot;}" data-flg="true">[

#### ...搜索树和链表的映射(Map)_实现_ - 以后我要当村长 - CSDN博客...

<div class="info-box d-flex align-content-center">

<span class="date">2-3</span>

</div>

2019年02月03日 16:46:57 以后我要当村长 阅读数:4 标签: Map的实现 ...【java】JavaFX从零开始实现拼图小游戏 个人分类 java笔记 17篇 数据结构 12...

](https://blog.csdn.net/qq_42370146/article/details/86760011)</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36812792/article/details/89038527,searchFromBaidu1_1,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36812792/article/details/89038527,searchFromBaidu1_1,-&quot;}" data-flg="true">[

#### _java_Swing做数字_拼图__小游戏_ - 温故而知新 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">5-14</span>

</div>

【java】JavaFX从零开始实现拼图小游戏 12-05 阅读数 437 最近java课老师布置...博文 来自: 以后我要当村长 python九宫格拼图小游戏 06-19 python小游戏,...

](https://blog.csdn.net/qq_36812792/article/details/89038527)</div>

<div class="recommend-item-box recommend-box-ident recommend-other-item-box" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://edu.csdn.net/course/detail/6975,BlogCommendClickRateRank_44&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://edu.csdn.net/course/detail/6975,BlogCommendClickRateRank_44&quot;}" data-flg="true">[

#### Unity3d开发跳一跳

<div class="info-box d-flex align-content-center"><span class="date">01-18</span></div>

<span class="desc oneline">-</span>

](https://edu.csdn.net/course/detail/6975)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/gj_user/article/details/54426418,BlogCommendFromQuerySearch_45&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/gj_user/article/details/54426418,BlogCommendFromQuerySearch_45&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _java__拼图__小游戏_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-14</span> <span class="read-num hover-hide">阅读数 661</span>

</div>

](https://blog.csdn.net/gj_user/article/details/54426418 "java拼图小游戏")

[<span class="desc oneline">一、该游戏一共有三个类1、</span>](https://blog.csdn.net/gj_user/article/details/54426418 "java拼图小游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">gj_user的博客</span>](https://blog.csdn.net/gj_user)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/fengsigaoju/article/details/51734863,BlogCommendFromQuerySearch_46&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/fengsigaoju/article/details/51734863,BlogCommendFromQuerySearch_46&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### _java_大作业之_拼图_游戏

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-22</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/fengsigaoju/article/details/51734863 "java大作业之拼图游戏")

[<span class="desc oneline">这个拼图游戏是帮同学做的，还是挺不错的，实现功能包括:自动选取图片，自动图片，且保证生成的一定有解，还有倒计时功能。先说下如何保证有解，两种方法：1，先切割然后自己后台让空格自己随机移动。      ...</span>](https://blog.csdn.net/fengsigaoju/article/details/51734863 "java大作业之拼图游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">fengsigaoju的博客</span>](https://blog.csdn.net/fengsigaoju)</span>

</div>

</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/cooperate456456/10328997,BlogCommendFromQuerySearch_47&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/cooperate456456/10328997,BlogCommendFromQuerySearch_47&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### android 简单_实现__拼图__小游戏_

<span class="data float-right">04-05</span></div>

<div class="desc oneline">android开发的拼图小游戏，最简单的实现，简单易懂</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/cooperate456456/10328997)</div>

<div class="recommend-item-box recommend-box-ident recommend-download-box clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/m0_37904844/9899371,BlogCommendFromQuerySearch_48&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://download.csdn.net/download/m0_37904844/9899371,BlogCommendFromQuerySearch_48&quot;}" data-flg="true">[

<div class="content clearfix">

<div class="">

#### h5_拼图_游戏

<span class="data float-right">07-14</span></div>

<div class="desc oneline">h5拼图游戏</div>

<span class="type-show type-show-download">下载</span></div>

](https://download.csdn.net/download/m0_37904844/9899371)</div>

<div class="recommend-item-box recommend-ad-box">

<div id="kp_box_68" data-pid="68" data-track-view="{&quot;mod&quot;:&quot;kp_popu_68-883&quot;,&quot;con&quot;:&quot;,,&quot;}" data-track-click="{&quot;mod&quot;:&quot;kp_popu_68-883&quot;,&quot;con&quot;:&quot;,,&quot;}"><script>// 渲染T48 传入 渲染位置的id和渲染位置的标记 p4CSDNRender_T("_4paradigm_T48_render", "T48");</script></div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_38630656/article/details/79601730,BlogCommendFromBaidu_49&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_38630656/article/details/79601730,BlogCommendFromBaidu_49&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 用_Java_FX写一个石头剪刀布的_小游戏_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-18</span> <span class="read-num hover-hide">阅读数 744</span>

</div>

](https://blog.csdn.net/qq_38630656/article/details/79601730 "用JavaFX写一个石头剪刀布的小游戏")

[<span class="desc oneline">用JavaFX写一个石头剪刀布的小游戏课程上布置的作业，其实java很少用来写这种程序的-GUI界面部分-石头剪刀布的逻辑部分书上教的是JavaFX，其实还有很多方法，书上说AWT和Swing基本上淘...</span>](https://blog.csdn.net/qq_38630656/article/details/79601730 "用JavaFX写一个石头剪刀布的小游戏") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">永远年轻，永远装嫩，永远不知好歹，永远热泪盈眶...</span>](https://blog.csdn.net/qq_38630656)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/maoyuanming0806/article/details/78067446,BlogCommendHotData_0&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/maoyuanming0806/article/details/78067446,BlogCommendHotData_0&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 搭建图片服务器《二》-linux安装nginx

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-22</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/maoyuanming0806/article/details/78067446 "搭建图片服务器《二》-linux安装nginx")

[<span class="desc oneline">nginx是个好东西，Nginx (engine x) 是一个高性能的HTTP和反向代理服务器，也是一个IMAP/POP3/SMTP服务器。Nginx是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambl...</span>](https://blog.csdn.net/maoyuanming0806/article/details/78067446 "搭建图片服务器《二》-linux安装nginx") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">maoyuanming0806的博客</span>](https://blog.csdn.net/maoyuanming0806)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36892341/article/details/73918672,BlogCommendHotData_1&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36892341/article/details/73918672,BlogCommendHotData_1&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### linux上安装Docker(非常简单的安装方法)

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-29</span> <span class="read-num hover-hide">阅读数 28万+</span>

</div>

](https://blog.csdn.net/qq_36892341/article/details/73918672 "linux上安装Docker(非常简单的安装方法)")

[<span class="desc oneline">最近比较有空，大四出来实习几个月了，作为实习狗的我，被叫去研究Docker了，汗汗！ Docker的三大核心概念：镜像、容器、仓库 镜像：类似虚拟机的镜像、用俗话说就是安装文件。 容器：类似一个轻量...</span>](https://blog.csdn.net/qq_36892341/article/details/73918672 "linux上安装Docker(非常简单的安装方法)") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">我走小路的博客</span>](https://blog.csdn.net/qq_36892341)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yimixgg/article/details/87808102,BlogCommendHotData_2&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yimixgg/article/details/87808102,BlogCommendHotData_2&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### BPSK、8PSK、QPSK、16QAM、64QAM区别与联系

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-20</span> <span class="read-num hover-hide">阅读数 1345</span>

</div>

](https://blog.csdn.net/yimixgg/article/details/87808102 "BPSK、8PSK、QPSK、16QAM、64QAM区别与联系")

[<span class="desc oneline">参考博文链接：https://blog.csdn.net/rhel_admin/article/details/50245785 这些是通信系统中的调制方式：BPSK：Binary Phase Sh...</span>](https://blog.csdn.net/yimixgg/article/details/87808102 "BPSK、8PSK、QPSK、16QAM、64QAM区别与联系") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">yimixgg的博客</span>](https://blog.csdn.net/yimixgg)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/silentpebble/article/details/41279285,BlogCommendHotData_3&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/silentpebble/article/details/41279285,BlogCommendHotData_3&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### centos 查看命令源码

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-19</span> <span class="read-num hover-hide">阅读数 13万+</span>

</div>

](https://blog.csdn.net/silentpebble/article/details/41279285 "centos 查看命令源码")

[<span class="desc oneline"># yum install yum-utils 设置源: [base-src] name=CentOS-5.4 - Base src - baseurl=http://vault.ce...</span>](https://blog.csdn.net/silentpebble/article/details/41279285 "centos 查看命令源码") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">linux/unix</span>](https://blog.csdn.net/silentpebble)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Main_Stage/article/details/41989499,BlogCommendHotData_4&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Main_Stage/article/details/41989499,BlogCommendHotData_4&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### Android圆形图片--自定义控件

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-17</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/Main_Stage/article/details/41989499 "Android圆形图片--自定义控件")

[<span class="desc oneline">Android圆形图片--自定义控件</span>](https://blog.csdn.net/Main_Stage/article/details/41989499 "Android圆形图片--自定义控件") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Main_Stage的专栏</span>](https://blog.csdn.net/Main_Stage)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hjimce/article/details/50866313,BlogCommendHotData_5&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hjimce/article/details/50866313,BlogCommendHotData_5&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 深度学习（二十九）Batch Normalization 学习笔记

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-12</span> <span class="read-num hover-hide">阅读数 17万+</span>

</div>

](https://blog.csdn.net/hjimce/article/details/50866313 "深度学习（二十九）Batch Normalization 学习笔记")

[<span class="desc oneline">近年来深度学习捷报连连，声名鹊起，随机梯度下架成了训练深度网络的主流方法。尽管随机梯度下降法，将对于训练深度网络，简单高效，但是它有个毛病，就是需要我们人为的去选择参数，比如学习率、参数初始化等，这些...</span>](https://blog.csdn.net/hjimce/article/details/50866313 "深度学习（二十九）Batch Normalization 学习笔记") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">hjimce的专栏</span>](https://blog.csdn.net/hjimce)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zhoudaxia/article/details/30919201,BlogCommendHotData_6&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zhoudaxia/article/details/30919201,BlogCommendHotData_6&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 面向切面编程(3)：AOP实现机制

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-23</span> <span class="read-num hover-hide">阅读数 3733</span>

</div>

](https://blog.csdn.net/zhoudaxia/article/details/30919201 "面向切面编程(3)：AOP实现机制")

[<span class="desc oneline">1 AOP各种的实现 AOP就是面向切面编程，我们可以从几个层面来实现AOP。</span>](https://blog.csdn.net/zhoudaxia/article/details/30919201 "面向切面编程(3)：AOP实现机制") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Jack Zhou的专栏</span>](https://blog.csdn.net/zhoudaxia)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/kevin66654/article/details/43269709,BlogCommendHotData_7&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/kevin66654/article/details/43269709,BlogCommendHotData_7&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### Kuangbin Flying 6最小生成树专题

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-29</span> <span class="read-num hover-hide">阅读数 1790</span>

</div>

](https://blog.csdn.net/kevin66654/article/details/43269709 "Kuangbin Flying 6最小生成树专题")

[<span class="desc oneline">kuangbin带你飞系列专题六最小生成树题解报告</span>](https://blog.csdn.net/kevin66654/article/details/43269709 "Kuangbin Flying 6最小生成树专题") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">ACdream</span>](https://blog.csdn.net/kevin66654)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq422733429/article/details/51280020,BlogCommendHotData_8&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq422733429/article/details/51280020,BlogCommendHotData_8&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### java通过SMTP发送QQ邮件的完全步骤

<div class="info-box d-flex align-content-center">

<span class="date hover-show">04-29</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/qq422733429/article/details/51280020 "java通过SMTP发送QQ邮件的完全步骤")

[<span class="desc oneline">java通过SMTP发送QQ邮件的完全步骤。本文是日常开发的随手记录，如有问题，请博内留言以帮助我改正和完善，一起努力，一起学习，一起进步！...</span>](https://blog.csdn.net/qq422733429/article/details/51280020 "java通过SMTP发送QQ邮件的完全步骤") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Mr peter king 的博客</span>](https://blog.csdn.net/qq422733429)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ymj7150697/article/details/7384126,BlogCommendHotData_9&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ymj7150697/article/details/7384126,BlogCommendHotData_9&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### expat介绍文档翻译

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-22</span> <span class="read-num hover-hide">阅读数 7万+</span>

</div>

](https://blog.csdn.net/ymj7150697/article/details/7384126 "expat介绍文档翻译")

[<span class="desc oneline">原文地址：http://www.xml.com/pub/a/1999/09/expat/index.html 因为需要用，所以才翻译了这个文档。但总归赖于英语水平很有限，翻译出来的中文有可能...</span>](https://blog.csdn.net/ymj7150697/article/details/7384126 "expat介绍文档翻译") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">ymj7150697的专栏</span>](https://blog.csdn.net/ymj7150697)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/themagickeyjianan/article/details/52386981,BlogCommendHotData_10&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/themagickeyjianan/article/details/52386981,BlogCommendHotData_10&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### python图片处理类之~PIL.Image模块(ios android icon图标自动生成处理)

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-31</span> <span class="read-num hover-hide">阅读数 11万+</span>

</div>

](https://blog.csdn.net/themagickeyjianan/article/details/52386981 "python图片处理类之~PIL.Image模块(ios android icon图标自动生成处理)")

[<span class="desc oneline">1.从pyCharm提示下载PIL包  http://www.pythonware.com/products/pil/   2.解压后，进入到目录下 cd /Users/jianan/Dow...</span>](https://blog.csdn.net/themagickeyjianan/article/details/52386981 "python图片处理类之~PIL.Image模块(ios android icon图标自动生成处理)") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">专注于cocos+unity+服务器全栈</span>](https://blog.csdn.net/themagickeyjianan)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yenange/article/details/12198829,BlogCommendHotData_11&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yenange/article/details/12198829,BlogCommendHotData_11&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### ODAC (odp.net) 从开发到部署

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-30</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/yenange/article/details/12198829 "ODAC (odp.net)  从开发到部署")

[<span class="desc oneline">test</span>](https://blog.csdn.net/yenange/article/details/12198829 "ODAC (odp.net)  从开发到部署") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">我想我是海 冬天的大海 心情随风轻摆</span>](https://blog.csdn.net/yenange)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qilixuening/article/details/77503631,BlogCommendHotData_12&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qilixuening/article/details/77503631,BlogCommendHotData_12&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### win10下配置GPU加速的Keras框架

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-23</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/qilixuening/article/details/77503631 "win10下配置GPU加速的Keras框架")

[<span class="desc oneline">不久之前，开始学习深度学习，这个时候发现用CPU计算的Keras框架性能明显不够用了，但当时随便弄了一下没能成功实现GPU加速。于是后来一次重装系统，从头详细地重现这个过程。Python环境搭建要搭建...</span>](https://blog.csdn.net/qilixuening/article/details/77503631 "win10下配置GPU加速的Keras框架") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">qilixuening的博客</span>](https://blog.csdn.net/qilixuening)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hayixia606/article/details/79237220,BlogCommendHotData_13&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hayixia606/article/details/79237220,BlogCommendHotData_13&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-02</span> <span class="read-num hover-hide">阅读数 18万+</span>

</div>

](https://blog.csdn.net/hayixia606/article/details/79237220 "微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用")

[<span class="desc oneline">扫二维码关注，获取更多技术分享 本文承接之前发布的博客《 微信支付V3微信公众号支付PHP教程/thinkPHP5公众号支付》必须阅读上篇文章后才可以阅读这篇文章。由于最近一段时间工作比较忙，...</span>](https://blog.csdn.net/hayixia606/article/details/79237220 "微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Marswill</span>](https://blog.csdn.net/hayixia606)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/q383965374/article/details/41249959,BlogCommendHotData_14&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/q383965374/article/details/41249959,BlogCommendHotData_14&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### maven项目生成的war包在tomcat下运行报错

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-19</span> <span class="read-num hover-hide">阅读数 4万+</span>

</div>

](https://blog.csdn.net/q383965374/article/details/41249959 "maven项目生成的war包在tomcat下运行报错")

[<span class="desc oneline">maven项目在tomcat</span>](https://blog.csdn.net/q383965374/article/details/41249959 "maven项目生成的war包在tomcat下运行报错") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">直到世界的尽头</span>](https://blog.csdn.net/q383965374)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011860731/article/details/48733073,BlogCommendHotData_15&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011860731/article/details/48733073,BlogCommendHotData_15&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### ThreadLocal的设计理念与作用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-25</span> <span class="read-num hover-hide">阅读数 9万+</span>

</div>

](https://blog.csdn.net/u011860731/article/details/48733073 "ThreadLocal的设计理念与作用")

[<span class="desc oneline">Java中的ThreadLocal类允许我们创建只能被同一个线程读写的变量。因此，如果一段代码含有一个ThreadLocal变量的引用，即使两个线程同时执行这段代码，它们也无法访问到对方的Thread...</span>](https://blog.csdn.net/u011860731/article/details/48733073 "ThreadLocal的设计理念与作用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">u011860731的专栏</span>](https://blog.csdn.net/u011860731)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wuchengzeng/article/details/50037611,BlogCommendHotData_16&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wuchengzeng/article/details/50037611,BlogCommendHotData_16&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### jquery/js实现一个网页同时调用多个倒计时(最新的)

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-25</span> <span class="read-num hover-hide">阅读数 53万+</span>

</div>

](https://blog.csdn.net/wuchengzeng/article/details/50037611 "jquery/js实现一个网页同时调用多个倒计时(最新的)")

[<span class="desc oneline">jquery/js实现一个网页同时调用多个倒计时(最新的) 最近需要网页添加多个倒计时. 查阅网络,基本上都是千遍一律的不好用. 自己按需写了个.希望对大家有用. 有用请赞一个哦! //js ...</span>](https://blog.csdn.net/wuchengzeng/article/details/50037611 "jquery/js实现一个网页同时调用多个倒计时(最新的)") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Websites</span>](https://blog.csdn.net/wuchengzeng)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendHotData_17&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendHotData_17&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 关于SpringBoot bean无法注入的问题（与文件包位置有关）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-16</span> <span class="read-num hover-hide">阅读数 26万+</span>

</div>

](https://blog.csdn.net/gefangshuai/article/details/50328451 "关于SpringBoot bean无法注入的问题（与文件包位置有关）")

[<span class="desc oneline">问题场景描述整个项目通过Maven构建，大致结构如下： 核心Spring框架一个module spring-boot-base service和dao一个module server-core 提供系统...</span>](https://blog.csdn.net/gefangshuai/article/details/50328451 "关于SpringBoot bean无法注入的问题（与文件包位置有关）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">开发随笔</span>](https://blog.csdn.net/gefangshuai)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq574857122/article/details/16361033,BlogCommendHotData_18&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq574857122/article/details/16361033,BlogCommendHotData_18&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 强连通分量及缩点tarjan算法解析

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-16</span> <span class="read-num hover-hide">阅读数 66万+</span>

</div>

](https://blog.csdn.net/qq574857122/article/details/16361033 "强连通分量及缩点tarjan算法解析")

[<span class="desc oneline">强连通分量： 简言之 就是找环（每条边只走一次，两两可达） 孤立的一个点也是一个连通分量   使用tarjan算法 在嵌套的多个环中优先得到最大环( 最小环就是每个孤立点）   定义： int Ti...</span>](https://blog.csdn.net/qq574857122/article/details/16361033 "强连通分量及缩点tarjan算法解析") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">九野的博客</span>](https://blog.csdn.net/qq574857122)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u012124438/article/details/53371102,BlogCommendHotData_19&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u012124438/article/details/53371102,BlogCommendHotData_19&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### Android中使用WebView与JS交互全解析

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-28</span> <span class="read-num hover-hide">阅读数 6853</span>

</div>

](https://blog.csdn.net/u012124438/article/details/53371102 "Android中使用WebView与JS交互全解析")

[<span class="desc oneline">1.概述首先，需要提出一个概念，那就是hybrid，主要意思就是native原生Android和h5混合开发。为什么要这样做呢？大家可以想象一下针对于同一个活动，如果使用纯native的开发方式，An...</span>](https://blog.csdn.net/u012124438/article/details/53371102 "Android中使用WebView与JS交互全解析") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">一个码农的博客</span>](https://blog.csdn.net/u012124438)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ch_liu23/article/details/53558549,BlogCommendHotData_20&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ch_liu23/article/details/53558549,BlogCommendHotData_20&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### YOLOv2训练自己的数据集（VOC格式）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-10</span> <span class="read-num hover-hide">阅读数 5万+</span>

</div>

](https://blog.csdn.net/ch_liu23/article/details/53558549 "YOLOv2训练自己的数据集（VOC格式）")

[<span class="desc oneline">最近在用yolo来做视频中的人员检测，选择YOLO是从速度考虑，在训练数据集的过程中碰到很多坑，并且现在yolo又到了v2的版本，在网络和命令中都有区别...</span>](https://blog.csdn.net/ch_liu23/article/details/53558549 "YOLOv2训练自己的数据集（VOC格式）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">ch_liu23的博客</span>](https://blog.csdn.net/ch_liu23)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Tiaaaaa/article/details/58116346,BlogCommendHotData_21&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Tiaaaaa/article/details/58116346,BlogCommendHotData_21&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### R语言逻辑回归、ROC曲线和十折交叉验证

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-27</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/Tiaaaaa/article/details/58116346 "R语言逻辑回归、ROC曲线和十折交叉验证")

[<span class="desc oneline">自己整理编写的逻辑回归模板，作为学习笔记记录分享。数据集用的是14个自变量Xi，一个因变量Y的australian数据集。 1\. 测试集和训练集3、7分组 australian ...</span>](https://blog.csdn.net/Tiaaaaa/article/details/58116346 "R语言逻辑回归、ROC曲线和十折交叉验证") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Tiaaaaa的博客</span>](https://blog.csdn.net/Tiaaaaa)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yiziweiyang/article/details/52516312,BlogCommendHotData_22&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yiziweiyang/article/details/52516312,BlogCommendHotData_22&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### MFC----MFC添加excel类库ole库，执行简单读写

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-12</span> <span class="read-num hover-hide">阅读数 1954</span>

</div>

](https://blog.csdn.net/yiziweiyang/article/details/52516312 "MFC----MFC添加excel类库ole库，执行简单读写")

[<span class="desc oneline">mfc操作excel方法一般有两种，一种是用odbc操作，另一种就是本文的加入excel类库操作 1\.    选择Menu-> View-> ClassWizade，打开ClassWizade...</span>](https://blog.csdn.net/yiziweiyang/article/details/52516312 "MFC----MFC添加excel类库ole库，执行简单读写") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">yiziweiyang的专栏</span>](https://blog.csdn.net/yiziweiyang)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xu__cg/article/details/52970885,BlogCommendHotData_23&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xu__cg/article/details/52970885,BlogCommendHotData_23&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### Java设计模式学习06——静态代理与动态代理

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-30</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/xu__cg/article/details/52970885 "Java设计模式学习06——静态代理与动态代理")

[<span class="desc oneline">一、代理模式为某个对象提供一个代理，从而控制这个代理的访问。代理类和委托类具有共同的父类或父接口，这样在任何使用委托类对象的地方都可以使用代理类对象替代。代理类负责请求的预处理、过滤、将请求分配给委托...</span>](https://blog.csdn.net/xu__cg/article/details/52970885 "Java设计模式学习06——静态代理与动态代理") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">小小本科生成长之路</span>](https://blog.csdn.net/xu__cg)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/luomingjun12315/article/details/45479073,BlogCommendHotData_24&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/luomingjun12315/article/details/45479073,BlogCommendHotData_24&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### 组合博弈 -- 三大基本博弈

<div class="info-box d-flex align-content-center">

<span class="date hover-show">05-04</span> <span class="read-num hover-hide">阅读数 6492</span>

</div>

](https://blog.csdn.net/luomingjun12315/article/details/45479073 "组合博弈 -- 三大基本博弈")

[<span class="desc oneline">这几天开始学习博弈，发现这一块是个难啃的骨头。以下是我从网上收集的资料汇总：        我国民间有个古老的游戏：就是有物品若干堆，（物品可以是火柴，围棋都可以）。两个人轮流从堆中取若干件，规定取光...</span>](https://blog.csdn.net/luomingjun12315/article/details/45479073 "组合博弈 -- 三大基本博弈") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Enstein_Jun</span>](https://blog.csdn.net/luomingjun12315)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yu_xiaofei/article/details/13287899,BlogCommendHotData_25&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yu_xiaofei/article/details/13287899,BlogCommendHotData_25&quot;}" data-flg="true">

<div class="content" style="width: 962px;">[

#### SNMP协议详解<二>

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-29</span> <span class="read-num hover-hide">阅读数 15万+</span>

</div>

](https://blog.csdn.net/yu_xiaofei/article/details/13287899 "SNMP协议详解<二>")

[<span class="desc oneline">上一篇文章讲解了SNMP的基本架构，本篇文章将重点分析SNMP报文，并对不同版本（SNMPv1、v2c、v3）进行区别！ 四、SNMP协议数据单元 在SNMP管理中，管理站（NMS）和代理（Age...</span>](https://blog.csdn.net/yu_xiaofei/article/details/13287899 "SNMP协议详解<二>") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">假装在纽约</span>](https://blog.csdn.net/yu_xiaofei)</span>

</div>

</div>

<div class="recommend-item-box type_hot_word">

<div class="content clearfix" style="width: 962px;">

<div class="word float-left"><span>[设计制作学习](https://edu.csdn.net/combos/o363_l0_t ) </span><span>[机器学习教程](https://edu.csdn.net/courses/o5329_s5330_k ) </span><span>[Objective-C培训](https://edu.csdn.net/courses/o280_s351_k ) </span><span>[交互设计视频教程](https://edu.csdn.net/combos/o7115_s388_l0_t ) </span><span>[颜色模型](https://edu.csdn.net/course/play/5599/104252 )</span></div>

</div>

<div class="content clearfix" style="width: 962px;">

<div class="float-left"><span>[mysql关联查询两次本表](https://www.csdn.net/gather_24/MtTaEg3sMDM5MS1ibG9n.html)</span> <span>[native底部 react](https://www.csdn.net/gather_10/MtjaIg3sMTUzMy1kb3dubG9hZAO0O0OO0O0O.html)</span> <span>[extjs glyph 图标](https://www.csdn.net/gather_1b/Ntzagg1sOTU3LWRvd25sb2Fk.html)</span> <span>[java课程设计拼图](https://www.csdn.net/gather_4a/NtzaEg4sMTMtZWR1.html)</span> <span>[java学习(从零开始)](https://www.csdn.net/gather_4a/NtzaQgwsNzAtZWR1.html)</span></div>

</div>

</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ranmudaofa/article/details/20842017,searchFromBaidu1_2,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ranmudaofa/article/details/20842017,searchFromBaidu1_2,-&quot;}" data-flg="true">[

#### _Java_FX游戏开发--第一课 精灵动画 - 燃木刀法 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">4-30</span>

</div>

【java】JavaFX从零开始实现拼图小游戏 12-05 阅读数 419 最近java课老师布置...博文 来自: 以后我要当村长 自己编程写的JavaFX 演示游戏,请大家看看 01-0...

](https://blog.csdn.net/ranmudaofa/article/details/20842017)</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/caomage/article/details/88847716,searchFromBaidu1_3,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_614&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/caomage/article/details/88847716,searchFromBaidu1_3,-&quot;}" data-flg="true">[

#### 使用Vue做一个可自动_拼图_的_拼图__小游戏_(一) - 从入门到..._CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">5-22</span>

</div>

](http://blog.csdn.net/caomage/article/details/88847716)</div>

<div class="recommend-loading-box">![](https://csdnimg.cn/release/phoenix/images/feedLoading.gif)</div>

<div class="recommend-end-box">

没有更多推荐了，[返回首页](https://blog.csdn.net/)

</div>

</div>

</main>
