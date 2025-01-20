<template>
    <header>
        <div class="header-content">
            <h1 class="header-content__logo">КомбоБрокер</h1>
            <nav>
                <p>Консультация</p>
                <p>Ипотечный Калькулятор</p>
            </nav>
        </div>

    </header>
</template>

<style lang="scss" scoped>
header{
    display: flex;
    align-items:center ;  
    height: 90px;

}
.header-content{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 7vw;
    nav{
        display: flex;
        flex-direction: row;
        gap: 2vw;
    }
}
h1{
    color: white;
    font-size: clamp(1rem, 0.716rem + 0.758vw, 1.625rem);
    margin: 0;
}
p{
    color: white;
    font-size: clamp(0.625rem, 0.341rem + 0.758vw, 1.25rem);
    margin: 0;
    font-weight: 300;
}

</style>