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

```java
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
 

public class Start extends Application {
 
	@Override
	public void start(Stage primaryStage) {
		try {
			// 父容器
			VBox vBox = new VBox();
 
			// 子容器,分别是按钮和输出文本
			HBox hBox_1 = new HBox();
			HBox hBox_2 = new HBox();
 
			// 显示难度选择按钮
			Button start_1 = new Button("简单");
			start_1.setOnAction(new EventHandler<ActionEvent>() {
				@Override
				public void handle(ActionEvent arg0) {
					// 打开另一个窗口，即游戏窗口
					Game_1 game_1 = new Game_1();
					game_1.start(new Stage());
					// 关闭开始界面
					primaryStage.close();
				}
			});
			Button start_2 = new Button("困难");
			start_2.setOnAction(new EventHandler<ActionEvent>() {
				@Override
				public void handle(ActionEvent arg0) {
					// 打开另一个窗口，即游戏窗口
					Game_2 game_2 = new Game_2();
					game_2.start(new Stage());
					// 关闭开始界面
					primaryStage.close();
				}
			});
			Button start_3 = new Button("地狱");
			start_3.setOnAction(new EventHandler<ActionEvent>() {
				@Override
				public void handle(ActionEvent arg0) {
					// 打开另一个窗口，即游戏窗口
					Game_3 game_3 = new Game_3();
					game_3.start(new Stage());
					// 关闭开始界面
					primaryStage.close();
				}
			});
 
			Label label = new Label("@余氏出品，必属渣品");
			//设置文本样式大小和颜色
			label.setFont(new Font("Arial", 30));
			label.setTextFill(Color.web("black"));
			
			hBox_1.getChildren().addAll(start_1, start_2, start_3);
			hBox_2.getChildren().add(label);
			vBox.getChildren().addAll(hBox_1, hBox_2);
 
			// 设置按钮大小并调节位置
			start_1.setPrefSize(100, 60);
			start_2.setPrefSize(100, 60);
			start_3.setPrefSize(100, 60);
			hBox_1.setPadding(new Insets(650, 100, 0, 175));
			hBox_2.setPadding(new Insets(50, 50, 500, 260));
			// 设置控件之间的距离
			hBox_1.setSpacing(100);
 
			// 标题栏图标
			Image image = new Image("application/4.jpg");
 
			Scene scene = new Scene(vBox, 800, 800);
			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());
			primaryStage.getIcons().add(image);
			primaryStage.setTitle("智障拼图");
			primaryStage.setScene(scene);
			primaryStage.setResizable(false);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
 
	public static void main(String[] args) {
		launch(args);
	}
}
```

**（2）简单难度的游戏界面 **

```java
   import java.util.Random;
 
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.geometry.Rectangle2D;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

public class Game_1 extends Application {
	public int m; // m是不在随机数组的那个数字
	ImageView[] imageViews = new ImageView[9];
 
	@Override
	public void start(Stage primaryStage) {
		init(primaryStage);
 
	}
 
	public void init(Stage primaryStage) {
		// 父布局
		VBox vBox = new VBox();
 
		// 3*3九宫格布局，作为上方的选项嵌套入父布局
		GridPane gridPane = new GridPane();
 
		// 水平布局，作为下方的选项嵌套入父布局
		HBox hbox = new HBox();
		hbox.setPadding(new Insets(10)); // 填充
		hbox.setAlignment(Pos.CENTER); // 居中
 
		// 添加3个点击
		Button home = new Button("返回首页");
		home.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即首页窗口
				Start start = new Start();
				start.start(new Stage());
				// 关闭原本界面
				primaryStage.close();
			}
		});
		Button again = new Button("重新游戏");
		again.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即游戏窗口
				Game_1 game = new Game_1();
				game.start(new Stage());
				// 关闭原本界面
				primaryStage.close();
			}
		});
		Button look = new Button("查看原图");
		look.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即显示原图
				OnImage_1 OnImage = new OnImage_1();
				OnImage.start(new Stage());
			}
		});
		// 设置按钮大小并居中
		home.setPrefSize(200, 50);
		again.setPrefSize(200, 50);
		look.setPrefSize(200, 50);
		// 设置控件之间的距离
		hbox.setSpacing(100);
 
		hbox.getChildren().addAll(home,again, look);
 
		// 游戏部分
		/*
		 * 自定义的函数，产生逆序数为偶数的不重复数组,依次作为图片数组的下标，例如: 2 0 1 3 4 5 6 7 ------>，此时m=8,变成如下即为正确：
		 * 0 1 2 3 4 5 4 7
		 */
		int[] n = random();
 
		Image image2 = new Image("application/2.jpg");
 
		for (int i = 0; i < 9; i++) {
			imageViews[i] = new ImageView(image2); // 初始化数组
			imageViews[i].setOnMouseClicked(new myevent()); // 设置点击事件
		}
		for (int i = 0, k = 0; i <= 2; i++) {
			for (int j = 0; j <= 2; j++, k++) {
				imageViews[k].setViewport(new Rectangle2D(250 * j, 250 * i, 250, 250)); // 切割图片分配给图片数组
			}
		}
		// 按照产生的随机数将imageView数组加入面板
		gridPane.add(imageViews[n[0]], 0, 0);
		gridPane.add(imageViews[n[1]], 1, 0);
		gridPane.add(imageViews[n[2]], 2, 0);
		gridPane.add(imageViews[n[3]], 0, 1);
		gridPane.add(imageViews[n[4]], 1, 1);
		gridPane.add(imageViews[n[5]], 2, 1);
		gridPane.add(imageViews[n[6]], 0, 2);
		gridPane.add(imageViews[n[7]], 1, 2);
		m = findnum(n); // 找出那个不在随机数组里面的数字
 
		Image image1 = new Image("application/3.jpg"); // 3.png为一个透明图，放在空格子中
		imageViews[m].setImage(image1);
		gridPane.add(imageViews[m], 2, 2);
		gridPane.setGridLinesVisible(true);
		gridPane.setPrefWidth(800);
		gridPane.setPrefHeight(700);
		vBox.getChildren().add(gridPane);
		// 布局嵌套，选项部分
		vBox.getChildren().add(hbox);
 
		// 标题栏图标
		Image image = new Image("application/4.jpg");
 
		Scene scene = new Scene(vBox, 800, 800);
		scene.getStylesheets().add(getClass().getResource("Game.css").toExternalForm());
		primaryStage.getIcons().add(image);
		primaryStage.setTitle("智障拼图");
		primaryStage.setScene(scene);
		primaryStage.setResizable(false);
		primaryStage.show();
	}
 
	public int[] random() { // 生成8个不重复的逆序数为偶数的数字,这样拼图才有结
		int[] ran = new int[8];
		while (iso(ran) == false) {
			ran = random_num();
		}
		return ran;
 
	}
 
	public int[] random_num() { // 生成8个不重复数
		int r[] = new int[8];
		Random random = new Random();
		for (int i = 0; i < 8; ++i) {
			r[i] = random.nextInt(9);
			for (int j = 0; j < i; ++j) {
				while (r[i] == r[j]) {
					i--;
					break;
				}
			}
		}
		return r;
	}
 
	// 判断逆序数是否为偶数
	public boolean iso(int[] num) {
		int sum = 0;
		for (int i = 0; i <= 6; ++i) {
			for (int j = i; j <= 7; j++) {
				if (num[i] > num[j]) {
					sum++;
				}
			}
		}
		if ((sum % 2) == 0 && sum != 0) {
			return true;
		}
 
		return false;
 
	}
 
	// 点击事件的实现
	class myevent implements EventHandler<MouseEvent> {
 
		@Override
		public void handle(MouseEvent arg0) {
 
			ImageView img = (ImageView) arg0.getSource();
			double sx = img.getLayoutX();
			double sy = img.getLayoutY();
			double dispx = sx - imageViews[m].getLayoutX();
			double dispy = sy - imageViews[m].getLayoutY();
			if ((dispx == -250) && (dispy == 0)) { // 点击的空格左边的格子
				swapimg(img, imageViews[m]); // 交换imageView
				if (issucc(imageViews)) { // 判断是否拼成功
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			}
 
			else if ((dispx == 0) && (dispy == -250)) { // 上面的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			} else if ((dispx == 250) && (dispy == 0)) { // 右边的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			} else if ((dispx == 0) && (dispy == 250)) { // 下面的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			}
		}
 
		// 交换两个imageView的实现
		public void swapimg(ImageView i1, ImageView i2) {
			int row1 = GridPane.getRowIndex(i1);
			int colu1 = GridPane.getColumnIndex(i1);
			int row2 = GridPane.getRowIndex(i2);
			int colu2 = GridPane.getColumnIndex(i2);
			GridPane.setRowIndex(i1, row2);
			GridPane.setColumnIndex(i1, colu2);
			GridPane.setRowIndex(i2, row1);
			GridPane.setColumnIndex(i2, colu1);
		}
	}
 
	// 判断是否拼图成功
	public boolean issucc(ImageView[] imageViews) {
		for (int i = 0; i <= 8; ++i) {
			if (i != 3 * GridPane.getRowIndex(imageViews[i]) + GridPane.getColumnIndex(imageViews[i])) {
				return false;
			}
		}
		return true;
	}
 
	// 找出m
	public int findnum(int[] n) {
		for (int j = 0; j <= 8; ++j) {
			if ((j == n[0]) || (j == n[1]) || (j == n[2]) || (j == n[3]) || (j == n[4]) || (j == n[5]) || (j == n[6])
					|| (j == n[7])) {
			} else {
				return j;
			}
		}
		return -1;
	}
 
}
```
**（3）困难难度的游戏界面 **

```java
   import java.util.Random;
 
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.geometry.Rectangle2D;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

public class Game_2 extends Application {
	public int m; // m是不在随机数组的那个数字
	ImageView[] imageViews = new ImageView[16];
 
	@Override
	public void start(Stage primaryStage) {
		init(primaryStage);
 
	}
 
	public void init(Stage primaryStage) {
		// 父布局
		VBox vBox = new VBox();
 
		// 3*3九宫格布局，作为上方的选项嵌套入父布局
		GridPane gridPane = new GridPane();
 
		// 水平布局，作为下方的选项嵌套入父布局
		HBox hbox = new HBox();
		hbox.setPadding(new Insets(10)); // 填充
		hbox.setAlignment(Pos.CENTER); // 居中
 
		// 添加3个点击
		Button home = new Button("返回首页");
		home.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即首页窗口
				Start start = new Start();
				start.start(new Stage());
				// 关闭原本界面
				primaryStage.close();
			}
		});
		Button again = new Button("重新游戏");
		again.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即游戏窗口
				Game_2 game = new Game_2();
				game.start(new Stage());
				// 关闭开始界面
				primaryStage.close();
			}
		});
		Button look = new Button("查看原图");
		look.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即显示原图
				OnImage_2 OnImage = new OnImage_2();
				OnImage.start(new Stage());
			}
		});
		// 设置按钮大小并居中
		home.setPrefSize(200, 50);
		again.setPrefSize(200, 50);
		look.setPrefSize(200, 50);
		// 设置控件之间的距离
		hbox.setSpacing(100);
 
		hbox.getChildren().addAll(home,again, look);
 
		// 游戏部分
		/*
		 * 自定义的函数，产生逆序数为偶数的不重复数组,依次作为图片数组的下标，例如: 2 0 1 3 4 5 6 7 ------>，此时m=8,变成如下即为正确：
		 * 0 1 2 3 4 5 4 7
		 */
		int[] n = random();
 
		Image image2 = new Image("application/2_1.jpg");
 
		for (int i = 0; i < 16; i++) {
			imageViews[i] = new ImageView(image2); // 初始化数组
			imageViews[i].setOnMouseClicked(new myevent()); // 设置点击事件
		}
		for (int i = 0, k = 0; i <= 3; i++) {
			for (int j = 0; j <= 3; j++, k++) {
				imageViews[k].setViewport(new Rectangle2D(150 * j, 150 * i, 150, 150)); // 切割图片分配给图片数组
			}
		}
		// 按照产生的随机数将imageView数组加入面板
		gridPane.add(imageViews[n[0]], 0, 0);
		gridPane.add(imageViews[n[1]], 1, 0);
		gridPane.add(imageViews[n[2]], 2, 0);
		gridPane.add(imageViews[n[3]], 3, 0);
		gridPane.add(imageViews[n[4]], 0, 1);
		gridPane.add(imageViews[n[5]], 1, 1);
		gridPane.add(imageViews[n[6]], 2, 1);
		gridPane.add(imageViews[n[7]], 3, 1);
		gridPane.add(imageViews[n[8]], 0, 2);
		gridPane.add(imageViews[n[9]], 1, 2);
		gridPane.add(imageViews[n[10]], 2, 2);
		gridPane.add(imageViews[n[11]], 3, 2);
		gridPane.add(imageViews[n[12]], 0, 3);
		gridPane.add(imageViews[n[13]], 1, 3);
		gridPane.add(imageViews[n[14]], 2, 3);
		m = findnum(n); // 找出那个不在随机数组里面的数字
 
		Image image1 = new Image("application/3.jpg"); // 3.png为一个透明图，放在空格子中
		imageViews[m].setImage(image1);
		gridPane.add(imageViews[m], 3, 3);
		gridPane.setGridLinesVisible(true);
		gridPane.setPrefWidth(800);
		gridPane.setPrefHeight(700);
		vBox.getChildren().add(gridPane);
		// 布局嵌套，选项部分
		vBox.getChildren().add(hbox);
 
		// 标题栏图标
		Image image = new Image("application/4.jpg");
 
		Scene scene = new Scene(vBox, 800, 800);
		scene.getStylesheets().add(getClass().getResource("Game.css").toExternalForm());
		primaryStage.getIcons().add(image);
		primaryStage.setTitle("智障拼图");
		primaryStage.setScene(scene);
		primaryStage.setResizable(false);
		primaryStage.show();
	}
 
	public int[] random() { // 生成15个不重复的逆序数为偶数的数字,这样拼图才有结
		int[] ran = new int[15];
		while (iso(ran) == false) {
			ran = random_num();
		}
		return ran;
 
	}
 
	public int[] random_num() { // 生成15个不重复数
		int r[] = new int[15];
		Random random = new Random();
		for (int i = 0; i < 15; ++i) {
			r[i] = random.nextInt(16);
			for (int j = 0; j < i; ++j) {
				while (r[i] == r[j]) {
					i--;
					break;
				}
			}
		}
		return r;
	}
 
	// 判断逆序数是否为偶数
	public boolean iso(int[] num) {
		int sum = 0;
		for (int i = 0; i <= 13; ++i) {
			for (int j = i; j <= 14; j++) {
				if (num[i] > num[j]) {
					sum++;
				}
			}
		}
		if ((sum % 2) == 0 && sum != 0) {
			return true;
		}
 
		return false;
 
	}
 
	// 点击事件的实现
	class myevent implements EventHandler<MouseEvent> {
 
		@Override
		public void handle(MouseEvent arg0) {
 
			ImageView img = (ImageView) arg0.getSource();
			double sx = img.getLayoutX();
			double sy = img.getLayoutY();
			double dispx = sx - imageViews[m].getLayoutX();
			double dispy = sy - imageViews[m].getLayoutY();
			if ((dispx == -150) && (dispy == 0)) { // 点击的空格左边的格子
				swapimg(img, imageViews[m]); // 交换imageView
				if (issucc(imageViews)) { // 判断是否拼成功
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			}
 
			else if ((dispx == 0) && (dispy == -150)) { // 上面的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			} else if ((dispx == 150) && (dispy == 0)) { // 右边的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			} else if ((dispx == 0) && (dispy == 150)) { // 下面的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			}
		}
 
		// 交换两个imageView的实现
		public void swapimg(ImageView i1, ImageView i2) {
			int row1 = GridPane.getRowIndex(i1);
			int colu1 = GridPane.getColumnIndex(i1);
			int row2 = GridPane.getRowIndex(i2);
			int colu2 = GridPane.getColumnIndex(i2);
			GridPane.setRowIndex(i1, row2);
			GridPane.setColumnIndex(i1, colu2);
			GridPane.setRowIndex(i2, row1);
			GridPane.setColumnIndex(i2, colu1);
		}
	}
 
	// 判断是否拼图成功
	public boolean issucc(ImageView[] imageViews) {
		for (int i = 0; i <= 15; ++i) {
			if (i != 3 * GridPane.getRowIndex(imageViews[i]) + GridPane.getColumnIndex(imageViews[i])) {
				return false;
			}
		}
		return true;
	}
 
	// 找出m
	public int findnum(int[] n) {
		for (int j = 0; j <= 15; ++j) {
			if ((j == n[0]) || (j == n[1]) || (j == n[2]) || (j == n[3]) || (j == n[4]) || (j == n[5]) || (j == n[6])
					|| (j == n[7])|| (j == n[8]) || (j == n[9]) || (j == n[10]) || (j == n[11]) || (j == n[12])
					|| (j == n[13]) || (j == n[14]) ) {
			} else {
				return j;
			}
		}
		return -1;
	}
 
}
```

**（4） 地狱难度的游戏界面**

```java
import java.util.Random;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.geometry.Rectangle2D;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
/**
*游戏界面----困难
*作者：Mr. Yu
*2018年12月5日,下午5:40:51
 */
public class Game_3 extends Application {
	public int m; // m是不在随机数组的那个数字
	ImageView[] imageViews = new ImageView[25];
 
	@Override
	public void start(Stage primaryStage) {
		init(primaryStage);
 
	}
 
	public void init(Stage primaryStage) {
		// 父布局
		VBox vBox = new VBox();
 
		// 3*3九宫格布局，作为上方的选项嵌套入父布局
		GridPane gridPane = new GridPane();
 
		// 水平布局，作为下方的选项嵌套入父布局
		HBox hbox = new HBox();
		hbox.setPadding(new Insets(10)); // 填充
		hbox.setAlignment(Pos.CENTER); // 居中
 
		// 添加3个点击
		Button home = new Button("返回首页");
		home.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即首页窗口
				Start start = new Start();
				start.start(new Stage());
				// 关闭原本界面
				primaryStage.close();
			}
		});
		Button again = new Button("重新游戏");
		again.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即游戏窗口
				Game_3 game = new Game_3();
				game.start(new Stage());
				// 关闭开始界面
				primaryStage.close();
			}
		});
		Button look = new Button("查看原图");
		look.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent arg0) {
				// 打开另一个窗口，即显示原图
				OnImage_3 OnImage = new OnImage_3();
				OnImage.start(new Stage());
			}
		});
		// 设置按钮大小并居中
		home.setPrefSize(200, 50);
		again.setPrefSize(200, 50);
		look.setPrefSize(200, 50);
		// 设置控件之间的距离
		hbox.setSpacing(100);
 
		hbox.getChildren().addAll(home, again, look);
 
		// 游戏部分
		/*
		 * 自定义的函数，产生逆序数为偶数的不重复数组,依次作为图片数组的下标，例如: 2 0 1 3 4 5 6 7 ------>，此时m=8,变成如下即为正确：
		 * 0 1 2 3 4 5 4 7
		 */
		int[] n = random();
 
		Image image2 = new Image("application/2_2.jpg");
 
		for (int i = 0; i < 25; i++) {
			imageViews[i] = new ImageView(image2); // 初始化数组
			imageViews[i].setOnMouseClicked(new myevent()); // 设置点击事件
		}
		for (int i = 0, k = 0; i <= 4; i++) {
			for (int j = 0; j <= 4; j++, k++) {
				imageViews[k].setViewport(new Rectangle2D(125 * j, 125 * i, 125, 125)); // 切割图片分配给图片数组
			}
		}
		// 按照产生的随机数将imageView数组加入面板
		gridPane.add(imageViews[n[0]], 0, 0);
		gridPane.add(imageViews[n[1]], 1, 0);
		gridPane.add(imageViews[n[2]], 2, 0);
		gridPane.add(imageViews[n[3]], 3, 0);
		gridPane.add(imageViews[n[4]], 4, 0);
		gridPane.add(imageViews[n[5]], 0, 1);
		gridPane.add(imageViews[n[6]], 1, 1);
		gridPane.add(imageViews[n[7]], 2, 1);
		gridPane.add(imageViews[n[8]], 3, 1);
		gridPane.add(imageViews[n[9]], 4, 1);
		gridPane.add(imageViews[n[10]], 0, 2);
		gridPane.add(imageViews[n[11]], 1, 2);
		gridPane.add(imageViews[n[12]], 2, 2);
		gridPane.add(imageViews[n[13]], 3, 2);
		gridPane.add(imageViews[n[14]], 4, 2);
		gridPane.add(imageViews[n[15]], 0, 3);
		gridPane.add(imageViews[n[16]], 1, 3);
		gridPane.add(imageViews[n[17]], 2, 3);
		gridPane.add(imageViews[n[18]], 3, 3);
		gridPane.add(imageViews[n[19]], 4, 3);
		gridPane.add(imageViews[n[20]], 0, 4);
		gridPane.add(imageViews[n[21]], 1, 4);
		gridPane.add(imageViews[n[22]], 2, 4);
		gridPane.add(imageViews[n[23]], 3, 4);
		m = findnum(n); // 找出那个不在随机数组里面的数字
 
		Image image1 = new Image("application/3.jpg"); // 3.png为一个透明图，放在空格子中
		imageViews[m].setImage(image1);
		gridPane.add(imageViews[m], 4, 4);
		gridPane.setGridLinesVisible(true);
		gridPane.setPrefWidth(800);
		gridPane.setPrefHeight(700);
		vBox.getChildren().add(gridPane);
		// 布局嵌套，选项部分
		vBox.getChildren().add(hbox);
 
		// 标题栏图标
		Image image = new Image("application/4.jpg");
 
		Scene scene = new Scene(vBox, 800, 800);
		scene.getStylesheets().add(getClass().getResource("Game.css").toExternalForm());
		primaryStage.getIcons().add(image);
		primaryStage.setTitle("智障拼图");
		primaryStage.setScene(scene);
		primaryStage.setResizable(false);
		primaryStage.show();
	}
 
	public int[] random() { // 生成24个不重复的逆序数为偶数的数字,这样拼图才有结
		int[] ran = new int[24];
		while (iso(ran) == false) {
			ran = random_num();
		}
		return ran;
 
	}
 
	public int[] random_num() { // 生成24个不重复数
		int r[] = new int[24];
		Random random = new Random();
		for (int i = 0; i < 24; ++i) {
			r[i] = random.nextInt(25);
			for (int j = 0; j < i; ++j) {
				while (r[i] == r[j]) {
					i--;
					break;
				}
			}
		}
		return r;
	}
 
	// 判断逆序数是否为偶数
	public boolean iso(int[] num) {
		int sum = 0;
		for (int i = 0; i <= 22; ++i) {
			for (int j = i; j <= 23; j++) {
				if (num[i] > num[j]) {
					sum++;
				}
			}
		}
		if ((sum % 2) == 0 && sum != 0) {
			return true;
		}
 
		return false;
 
	}
 
	// 点击事件的实现
	class myevent implements EventHandler<MouseEvent> {
 
		@Override
		public void handle(MouseEvent arg0) {
 
			ImageView img = (ImageView) arg0.getSource();
			double sx = img.getLayoutX();
			double sy = img.getLayoutY();
			double dispx = sx - imageViews[m].getLayoutX();
			double dispy = sy - imageViews[m].getLayoutY();
			if ((dispx == -125) && (dispy == 0)) { // 点击的空格左边的格子
				swapimg(img, imageViews[m]); // 交换imageView
				if (issucc(imageViews)) { // 判断是否拼成功
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			}
 
			else if ((dispx == 0) && (dispy == -125)) { // 上面的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			} else if ((dispx == 125) && (dispy == 0)) { // 右边的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			} else if ((dispx == 0) && (dispy == 125)) { // 下面的格子
				swapimg(img, imageViews[m]);
				if (issucc(imageViews)) {
					Alert alert = new Alert(AlertType.WARNING, "恭喜你，拼图成功！");
					alert.show();
				}
			}
		}
 
		// 交换两个imageView的实现
		public void swapimg(ImageView i1, ImageView i2) {
			int row1 = GridPane.getRowIndex(i1);
			int colu1 = GridPane.getColumnIndex(i1);
			int row2 = GridPane.getRowIndex(i2);
			int colu2 = GridPane.getColumnIndex(i2);
			GridPane.setRowIndex(i1, row2);
			GridPane.setColumnIndex(i1, colu2);
			GridPane.setRowIndex(i2, row1);
			GridPane.setColumnIndex(i2, colu1);
		}
	}
 
	// 判断是否拼图成功
	public boolean issucc(ImageView[] imageViews) {
		for (int i = 0; i <= 24; ++i) {
			if (i != 3 * GridPane.getRowIndex(imageViews[i]) + GridPane.getColumnIndex(imageViews[i])) {
				return false;
			}
		}
		return true;
	}
 
	// 找出m
	public int findnum(int[] n) {
		for (int j = 0; j <= 24; ++j) {
			if ((j == n[0]) || (j == n[1]) || (j == n[2]) || (j == n[3]) || (j == n[4]) || (j == n[5]) || (j == n[6])
					|| (j == n[7]) || (j == n[8]) || (j == n[9]) || (j == n[10]) || (j == n[11]) || (j == n[12])
					|| (j == n[13]) || (j == n[14]) || (j == n[15]) || (j == n[16]) || (j == n[17]) || (j == n[18])
					|| (j == n[19]) || (j == n[20]) || (j == n[21]) || (j == n[22]) || (j == n[23])) {
			} else {
				return j;
			}
		}
		return -1;
	}
 
}
```

**（5）简单难度显示原图界面 **

```java
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;

public class OnImage_1 extends Application {
 
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox vBox = new VBox();
			// 原图
			Image image1 = new Image("application/2.jpg");
			double width = image1.getWidth();
			double higth = image1.getHeight();
			ImageView imageView = new ImageView(image1);
			vBox.getChildren().add(imageView);
 
			// 标题栏图标
			Image image = new Image("application/4.jpg");
 
			Scene scene = new Scene(vBox, width, higth);
			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());
			primaryStage.getIcons().add(image);
			primaryStage.setTitle("智障拼图");
			primaryStage.setScene(scene);
			primaryStage.setResizable(false);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
}
```

**（6）困难难度显示原图界面 **

```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
 

public class OnImage_2 extends Application {
 
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox vBox = new VBox();
			// 原图
			Image image1 = new Image("application/2_1.jpg");
			double width = image1.getWidth();
			double higth = image1.getHeight();
			ImageView imageView = new ImageView(image1);
			vBox.getChildren().add(imageView);
 
			// 标题栏图标
			Image image = new Image("application/4.jpg");
 
			Scene scene = new Scene(vBox, width, higth);
			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());
			primaryStage.getIcons().add(image);
			primaryStage.setTitle("智障拼图");
			primaryStage.setScene(scene);
			primaryStage.setResizable(false);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
}
```

**（7）地狱难度显示原图界面 **

```java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
 

public class OnImage_3 extends Application {
 
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox vBox = new VBox();
			// 原图
			Image image1 = new Image("application/2_2.jpg");
			double width = image1.getWidth();
			double higth = image1.getHeight();
			ImageView imageView = new ImageView(image1);
			vBox.getChildren().add(imageView);
 
			// 标题栏图标
			Image image = new Image("application/4.jpg");
 
			Scene scene = new Scene(vBox, width, higth);
			scene.getStylesheets().add(getClass().getResource("Start.css").toExternalForm());
			primaryStage.getIcons().add(image);
			primaryStage.setTitle("智障拼图");
			primaryStage.setScene(scene);
			primaryStage.setResizable(false);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
}
```

**有几个点需要注意一下：(1)必须要装JAVAFX插件且JDK1.8或以上才可以运行，需要的可以找我提供内嵌了插件的Eclipse安装包**

**                                        (2)我的图片是存放在资源文件中，即在本包中，会被自动拷贝到bin目录下，大家的图片来源可以更换为本地图片或网址图片**

## <a name="t4"></a>**（五）后续**

**现在这个程序还是很简陋的，本来想美化一下界面，再完善一些功能，诸如倒计时，已走步数，精确提示，背景音乐播放，供玩家可选择的拼图图片等等，但是想想自己那么懒还是算了哈哈哈。**

</div>

</div>

</article>

</div>

