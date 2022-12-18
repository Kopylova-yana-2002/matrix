<html>
    <head>
        <title>Вычисление обратной матрицы</title>
    </head>
    <body>
        <h2>Вычисление обратной матрицы</h2>
        <form action="index.php" method="post">
        <b><label for="size_operand">Размер </label></b>
        </br>
        <input type="number" name="size" id="size" required>
        </br>
        </br>
        <b><label for="matrix_operand">Матрица </label></b>
        </br>
        <p>Строки в матрице разделяются символом '-', а числа в одной строке разделены символом '_'</p>
        <p>Пример для размера 2: 8_9-2_2</p>
        <input type="string" name="matrix" id="matrix" required>
        <input type="submit" value="RUN!">
        </form>
        <?php
            if (isset($_POST['size']) && isset($_POST['matrix'])){
            $myCurl = curl_init();
            curl_setopt_array($myCurl, array(
            CURLOPT_URL =>
            'http://nginxserver/api/inverse/?size='.$_POST['size'].'&matrix='.$_POST['matrix'],
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HEADER => false,
            ));
            $response = curl_exec($myCurl);
            curl_close($myCurl);

            echo "Ответ на Ваш запрос: ".$response;
            }
        ?>
    </body>
</html>
