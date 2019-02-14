class Coche {
    protected $color;
    public function setColor($color)
    {
        $this->color = $color;
    }
    public function getColor()
    {
        return $this->color;
    }
    public function printCaracteristicas()
    {
        echo 'Color: '. $this->getColor;
    }
}
